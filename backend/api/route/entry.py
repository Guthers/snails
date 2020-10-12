from .api_register import api_register

from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
from flask import request
from typing import Tuple, List

import flask

from api.db import db, Entry, Liked, User
from api.model import EntryModel, UserModel
from utils.route_utils import swag_param, PARAM_IN

@api_register.route('/entry', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'header',
        'name': 'x-uq-user',
        'type': 'string',
        'required': 'true'
    },
    swag_param(PARAM_IN.QUERY, "content", str),
    swag_param(PARAM_IN.QUERY, "reply_to", int),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Creates an entry',
            'schema': EntryModel.schema()
        },
        400: {
            'description': 'Invalid reply_to or content or x-uq-user',
        }
    }
})
def create_entry():
    student_id = request.headers.get("x-uq-user", None)
    content = request.args.get("content", None)
    reply_to = request.args.get("reply_to", None)

    if not student_id:
        return "Missing x-uq-user header", HTTPStatus.UNAUTHORIZED
    
    if not content:
        return "Missing content query parameter", HTTPStatus.BAD_REQUEST

    # The user making the entry must be in the database
    if User.query.get(student_id) is None:
        return "User not in database", HTTPStatus.BAD_REQUEST

    # If this is a reply to an entry, the parent entry must exist
    if reply_to is not None and Entry.query.get(reply_to) is None:
        return "reply_to is invalid or does not exist", HTTPStatus.BAD_REQUEST

    # Create the entry
    row = Entry(reply_id=reply_to, 
                author_id=student_id, 
                content=content,
                created_at=datetime.now())

    db.session.add(row)
    db.session.commit()

    entry = Entry.query.get(row.id)
    if entry is None:
        return None, HTTPStatus.INTERNAL_SERVER_ERROR

    response = create_entry_model(entry)

    return EntryModel.schema()().jsonify(response), HTTPStatus.CREATED



@api_register.route('/entry/<int:entry_id>', methods=["GET","DELETE"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entry_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the entry by the specified id',
            'schema': EntryModel.schema()
        }
    }
})
def get_entry(entry_id: int):
    entry = Entry.query.get(entry_id)
    if entry is None:
        return "entry_id not found", HTTPStatus.BAD_REQUEST

    response = create_entry_model(entry)

    if request.method == "DELETE":
        student_id = request.headers.get("x-uq-user", None)
        if student_id is None or student_id != entry.author_id:
            return "Invalid x-uq-user", HTTPStatus.UNAUTHORIZED
        db.session.delete(entry)
        db.session.commit()

        return '', HTTPStatus.NO_CONTENT
        
    return EntryModel.schema()().jsonify(response), HTTPStatus.OK


@api_register.route('/entry/replies/<int:entry_id>', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entry_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets a list of entries which are replies to the entry_id',
            'schema': EntryModel.schema()
        },
        400: {
            'description': 'Invalid entry_id',
        }
    }
})
def get_entry_replies(entry_id: int):
    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.BAD_REQUEST

    result = [create_entry_model(r) for r in entry.replies.order_by(Entry.created_at.desc())]

    return EntryModel.schema()().jsonify(result, many=True), HTTPStatus.OK


@api_register.route('/entry/like/<int:entry_id>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entry_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Like the specified entry',
            'schema': EntryModel.schema()
        },
        400: {
            'description': 'Invalid x-uq-user',
        },
        404: {
            'description': 'entry_id not found',
        },
    }
})
def like_entry(entry_id: int):
    student_id = request.headers.get("x-uq-user", None)
    if not student_id:
        return "Invalid x-uq-user", HTTPStatus.BAD_REQUEST

    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.NOT_FOUND

    # check student_id in database
    if User.query.get(student_id) is None:
        return "Invalid x-uq-user", HTTPStatus.BAD_REQUEST

    liked = Liked.query.get((entry_id, student_id))
    # Ignore duplicate entries
    if liked is None:
        row = Liked(entry_id=entry_id, user_id=student_id)

        db.session.add(row)
        db.session.commit()

    response = create_entry_model(entry)

    return EntryModel.schema()().jsonify(response), HTTPStatus.OK

@api_register.route('/entry/unlike/<int:entry_id>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entry_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Unlike the specified entry',
            'schema': EntryModel.schema()
        }
    }
})
def unlike_entry(entry_id: int):
    student_id = request.headers.get("x-uq-user", None)
    if not student_id:
        return "Invalid x-uq-user", HTTPStatus.BAD_REQUEST

    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.NOT_FOUND

    # check student_id in database
    if User.query.get(student_id) is None:
        return "Invalid x-uq-user", HTTPStatus.BAD_REQUEST


    liked = Liked.query.get((entry_id, student_id))
    # Fail silently
    if liked is not None:
        row = Liked(entry_id=entry_id, user_id=student_id)

        db.session.delete(liked)
        db.session.commit()

    response = create_entry_model(entry)

    return EntryModel.schema()().jsonify(response), HTTPStatus.OK

def create_entry_model(entry: Entry) -> EntryModel:
    liked_by = []

    for like in entry.likes:
        user = like.user  # type: User
        liked_by.append(UserModel(username=user.id,
                                  name=user.name, 
                                  user_id=user.id,
                                  created_at=user.created_at))

    replies = [r.id for r in entry.replies]
    user = entry.author # type: User

    author = UserModel(username=user.id,
                       name=user.name, 
                       user_id=user.id,
                       created_at=user.created_at)

    result = EntryModel(created_at=entry.created_at,
                        reply_to=entry.reply_id,
                        content=entry.content, 
                        liked_by=liked_by,
                        replies=replies, 
                        author=author,
                        entry_id=entry.id)

    return result
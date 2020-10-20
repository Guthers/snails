from .api_register import api_register

from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
from flask import request
from flask_praetorian import auth_required, current_user
from typing import Tuple, List

import flask

from api.db import db, Entry, Liked, User
from api.model import EntryModel, UserModel
from utils.route_utils import swag_param, PARAM, VALUE

@api_register.route('/entry', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.HEADER, "Authorization", VALUE.STRING),
        swag_param(PARAM.QUERY, "content", VALUE.STRING),
        swag_param(PARAM.QUERY, "reply_to", VALUE.INTEGER, required=False),
    ],
    'responses': {
        HTTPStatus.CREATED.value: {
            'description': 'Creates an entry',
            'schema': EntryModel.schema()
        },
    }
})
@auth_required
def create_entry():
    content = request.args.get("content", None)
    reply_to = request.args.get("reply_to", None)

    if not content:
        return "Missing content query parameter", HTTPStatus.BAD_REQUEST

    user = current_user() # type: User

    # If this is a reply to an entry, the parent entry must exist
    if reply_to is not None and Entry.query.get(reply_to) is None:
        return "reply_to is invalid or does not exist", HTTPStatus.BAD_REQUEST

    # Create the entry
    entry = Entry(reply_id=reply_to, 
                author_id=user.id, 
                content=content,
                created_at=datetime.now())

    db.session.add(entry)
    db.session.commit()

    response = create_entry_model(entry)

    return EntryModel.schema()().jsonify(response), HTTPStatus.CREATED


@api_register.route('/entries', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.QUERY, "count", VALUE.INTEGER, required=False),
        swag_param(PARAM.QUERY, "before[id]", VALUE.INTEGER, required=False),
        swag_param(PARAM.QUERY, "after[id]", VALUE.INTEGER, required=False),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Returns a list of entries in reverse-chronological order',
            'schema': {
                "type": "array",
                "items": EntryModel.schema()
            }
        }
    }
})
def get_entries():
    count = request.args.get("count", "20")
    before_id = request.args.get("before[id]", None)
    after_id = request.args.get("after[id]", None)

    if not count.isdigit():
        return "Invalid count", HTTPStatus.BAD_REQUEST

    count = int(count)
    
    if before_id is not None and not before_id.isdigit():
        return "Invalid before[id]", HTTPStatus.BAD_REQUEST

    if after_id is not None and not after_id.isdigit():
        return "Invalid after[id]", HTTPStatus.BAD_REQUEST

    before = Entry.query.get(before_id)
    after = Entry.query.get(after_id)
    subquery = Entry.query.order_by(Entry.id.desc()).filter(Entry.reply_id == None)
    if before: 
        subquery = subquery.filter(Entry.created_at < before.created_at)
    if after:
        subquery = subquery.filter(Entry.created_at > after.created_at)
    
    subquery = subquery.limit(count).all()

    response = [create_entry_model(e) for e in subquery]
        
    return EntryModel.schema()().jsonify(response, many=True), HTTPStatus.OK


@api_register.route('/entry/<int:entry_id>', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.PATH, "entry_id", VALUE.INTEGER),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get entry',
            'schema': EntryModel.schema()
        }
    }
})
def get_entry(entry_id: int):
    entry = Entry.query.get(entry_id)
    if entry is None:
        return "entry_id not found", HTTPStatus.BAD_REQUEST

    response = create_entry_model(entry)
        
    return EntryModel.schema()().jsonify(response), HTTPStatus.OK

@api_register.route('/entry/<int:entry_id>', methods=["DELETE"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.HEADER, "Authorization", VALUE.STRING),
        swag_param(PARAM.PATH, "entry_id", VALUE.INTEGER),
    ],
    'responses': {
        HTTPStatus.NO_CONTENT.value: {
            'description': 'Delete entry',
            'schema': EntryModel.schema()
        }
    }
})
@auth_required
def delete_entry(entry_id: VALUE.INTEGER):
    user = current_user()

    entry = Entry.query.get(entry_id)
    if entry is None:
        return "entry_id not found", HTTPStatus.BAD_REQUEST

    if user != entry.author_id:
        return "Unauthorized", HTTPStatus.UNAUTHORIZED
    
    db.session.delete(entry)
    db.session.commit()

    return '', HTTPStatus.NO_CONTENT



@api_register.route('/entry/replies/<int:entry_id>', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.PATH, "entry_id", VALUE.INTEGER),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get replies',
            'schema': {
                "type": "array",
                "items": EntryModel.schema()
            }
        },
    }
})
def get_entry_replies(entry_id: int):
    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.BAD_REQUEST

    result = [create_entry_model(r) for r in entry.replies.order_by(Entry.id.desc())]

    return EntryModel.schema()().jsonify(result, many=True), HTTPStatus.OK


@api_register.route('/entry/like/<int:entry_id>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.HEADER, "Authorization", VALUE.STRING),
        swag_param(PARAM.PATH, "entry_id", VALUE.INTEGER),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Like entry',
            'schema': EntryModel.schema()
        },
    }
})
@auth_required
def like_entry(entry_id: int):
    user = current_user() # type: User

    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.NOT_FOUND


    liked = Liked.query.get((entry_id, user.id))
    # Ignore duplicate entries
    if liked is None:
        row = Liked(entry_id=entry_id, user_id=user.id)

        db.session.add(row)
        db.session.commit()

    response = create_entry_model(entry)

    return EntryModel.schema()().jsonify(response), HTTPStatus.OK

@api_register.route('/entry/unlike/<int:entry_id>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
        swag_param(PARAM.HEADER, "Authorization", VALUE.STRING),
        swag_param(PARAM.PATH, "entry_id", VALUE.INTEGER),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Unlike entry',
            'schema': EntryModel.schema()
        }
    }
})
@auth_required
def unlike_entry(entry_id: int):
    user = current_user()

    entry = Entry.query.get(entry_id)
    if entry is None:
        return "Entry not found", HTTPStatus.NOT_FOUND


    liked = Liked.query.get((entry_id, user.id))
    # Fail silently
    if liked is not None:
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

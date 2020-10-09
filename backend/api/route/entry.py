from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
import api.model as models
import api.db as dbs
from .api_register import api_register

import flask
from flask import request
from utils.route_utils import swag_param, PARAM_IN

@api_register.route('/entry', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'header',
        'name': 'Authorization',
        'type': 'string',
        'required': 'false'
    },
    swag_param(PARAM_IN.QUERY, "content", str),
    swag_param(PARAM_IN.QUERY, "replyTo", int),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Creates an entry',
            'schema': models.EntryModel.schema()
        },
        400: {
            'description': 'Invalid replyTo or content or Authorization',
        }
    }
})
def entry():
    studentID = request.headers.get("x-uq-user", None)
    if not studentID:
        return "Invalid replyTo or content or Authorization", 400
    # check studentID in database
    if dbs.UserDB.query.filter_by(student_id=studentID).scalar() is None:
        return "Invalid replyTo or content or Authorization", 400

    content = request.args.get("content", None)
    if not content:
        return "Invalid replyTo or content or Authorization", 400

    replyTo = request.args.get("replyTo", None)
    # check replyTo is valid
    if replyTo is not None and (not replyTo.isdigit() or
            dbs.Epost.query.filter_by(post_id=int(replyTo)).scalar() is None):
        return "Invalid replyTo or content or Authorization", 400

    # create an entry
    row = dbs.Epost(reply_id=replyTo, author_id=studentID, content=content,
            create_date=datetime.now())

    dbs.db.session.add(row)
    dbs.db.session.commit()

    entry = dbs.Epost.query.filter_by(post_id=row.post_id).first()

    # append list of liked_by
    liked_by = []
    for like in entry.likes:
        user = like.user
        liked_by.append(models.UserModel(username=user.student_id,
            name=user.student_name, user_id=user.student_id,
            created_at=user.create_date))

    replies = [r.post_id for r in entry.replies]

    user = entry.author
    author = models.UserModel(username=user.student_id,
        name=user.student_name, user_id=user.student_id,
        created_at=user.create_date)

    result = models.EntryModel(created_at=entry.create_date,
            reply_to=entry.reply_id,
            content=entry.content, liked_by=liked_by,
            replies=replies, author=author,
            entry_id=entry.post_id)
    return models.EntryModel.schema()().jsonify(result), 200


@api_register.route('/entry/<int:entryID>', methods=["GET","DELETE"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the entry by the specified id',
            'schema': models.EntryModel.schema()
        }
    }
})
def entry_id(entryID: int):
    entry = dbs.Epost.query.filter_by(post_id=entryID).first()
    if entry is None:
        return "entryID not found", 404

    # append list of liked_by
    liked_by = []
    for like in entry.likes:
        user = like.user
        liked_by.append(models.UserModel(username=user.student_id,
            name=user.student_name, user_id=user.student_id,
            created_at=user.create_date))

    replies = [r.post_id for r in entry.replies]

    user = entry.author
    author = models.UserModel(username=user.student_id,
        name=user.student_name, user_id=user.student_id,
        created_at=user.create_date)

    result = models.EntryModel(created_at=entry.create_date,
            reply_to=entry.reply_id,
            content=entry.content, liked_by=liked_by,
            replies=replies, author=author,
            entry_id=entry.post_id)

    if request.method == "DELETE":
        studentID = request.headers.get("x-uq-user", None)
        if studentID is None or studentID != user.student_id:
            return "Invalid Authorization", 400
        dbs.db.session.delete(entry)
        dbs.db.session.commit()
        
    return models.EntryModel.schema()().jsonify(result), 200


@api_register.route('/entry/replies', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [
    swag_param(PARAM_IN.QUERY, "entryID", int),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets a list of entries which are replies to the entryID',
            'schema': models.EntryModel.schema()
        },
        400: {
            'description': 'Invalid entryID',
        }
    }
})
def entry_id_replies():
    entryID = request.args.get("entryID", None)
    if entryID is None or not entryID.isdigit():
        return "Invalid entryID", 400

    entry = dbs.Epost.query.filter_by(post_id=entryID).first()
    if entry is None:
        return "entryID not found", 404

    result = []

    for r in entry.replies:
        liked_by = []
        for like in r.likes:
            user = like.user
            liked_by.append({"username":user.student_id,
                    "name":user.student_name, "user_id":user.student_id,
                    "created_at":user.create_date})

        replies = [rr.post_id for rr in r.replies]

        user = r.author
        author = { "username": user.student_id,
                "name": user.student_name, "user_id": user.student_id,
                "created_at": user.create_date }

        result.append({"created_at": r.create_date,
            "reply_to": r.reply_id,
            "content": r.content, "liked_by": liked_by,
            "replies": replies, "author": author,
            "entry_id": r.post_id})

    return flask.json.jsonify(result), 200


@api_register.route('/entry/like/<int:entryID>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Like the specified entry',
            'schema': models.EntryModel.schema()
        },
        400: {
            'description': 'Invalid Authorization',
        },
        404: {
            'description': 'entryID not found',
        },
    }
})
def like_entry(entryID: int):
    entry = dbs.Epost.query.filter_by(post_id=entryID).first()
    if entry is None:
        return "entryID not found", 404

    studentID = request.headers.get("x-uq-user", None)
    if not studentID:
        return "Invalid Authorization", 400
    # check studentID in database
    if dbs.UserDB.query.filter_by(student_id=studentID).scalar() is None:
        return "Invalid Authorization", 400

    # check entry doesn't already exist
    if dbs.Liked.query.filter_by(post_id=entryID, user_id=studentID).scalar() is None:
        # create an entry
        row = dbs.Liked(post_id=entryID, user_id=studentID)

        dbs.db.session.add(row)
        dbs.db.session.commit()

    # append list of liked_by
    liked_by = []
    for like in entry.likes:
        user = like.user
        liked_by.append(models.UserModel(username=user.student_id,
            name=user.student_name, user_id=user.student_id,
            created_at=user.create_date))

    replies = [r.post_id for r in entry.replies]

    user = entry.author
    author = models.UserModel(username=user.student_id,
        name=user.student_name, user_id=user.student_id,
        created_at=user.create_date)

    result = models.EntryModel(created_at=entry.create_date,
            reply_to=entry.reply_id,
            content=entry.content, liked_by=liked_by,
            replies=replies, author=author,
            entry_id=entry.post_id)

    return models.EntryModel.schema()().jsonify(result), 200

@api_register.route('/entry/unlike/<int:entryID>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Unlike the specified entry',
            'schema': models.EntryModel.schema()
        }
    }
})
def unlike_entry(entryID: int):
    entry = dbs.Epost.query.filter_by(post_id=entryID).first()
    if entry is None:
        return "entryID not found", 404

    studentID = request.headers.get("x-uq-user", None)
    if not studentID:
        return "Invalid Authorization", 400
    # check studentID in database
    if dbs.UserDB.query.filter_by(student_id=studentID).scalar() is None:
        return "Invalid Authorization", 400
    like = dbs.Liked.query.filter_by(post_id=entryID, user_id=studentID).first()
    # check entry doesn't already exist
    if like is not None:
        dbs.db.session.delete(like)
        dbs.db.session.commit()

    # append list of liked_by
    liked_by = []
    for like in entry.likes:
        user = like.user
        liked_by.append(models.UserModel(username=user.student_id,
            name=user.student_name, user_id=user.student_id,
            created_at=user.create_date))

    replies = [r.post_id for r in entry.replies]

    user = entry.author
    author = models.UserModel(username=user.student_id,
        name=user.student_name, user_id=user.student_id,
        created_at=user.create_date)

    result = models.EntryModel(created_at=entry.create_date,
            reply_to=entry.reply_id,
            content=entry.content, liked_by=liked_by,
            replies=replies, author=author,
            entry_id=entry.post_id)

    return models.EntryModel.schema()().jsonify(result), 200

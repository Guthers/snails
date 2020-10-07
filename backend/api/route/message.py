from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
import itertools as it
import api.model as models
import api.db as dbs
from .api_register import api_register

import flask
import json
from flask import request
from utils.route_utils import swag_param, PARAM_IN

@api_register.route('/messages/<string:userID>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'List messages',
            'schema': models.MessageModel.schema()
        },
        404: {
            'description': 'userID not found',
        }
    }
})
def message_user_list(userID: str):
    result = []
    user = dbs.UserDB.query.filter_by(student_id=userID).first()
    if not user:
        return "userID not found", 404

    studentID = request.headers.get("x-uq-user", None)
    if studentID != userID:
        # search in user.messages_sent for messages to studentID
        for message in it.chain((m for m in user.messages_sent if m.to_user_id ==
            studentID), (m for m in user.messages_recv if m.from_user_id ==
                studentID)):
            # This is VERY ugly
            userTo = message.to_user
            resultTo = {"username":userTo.student_id,
                    "name":userTo.student_name, "user_id":userTo.student_id,
                    "created_at":userTo.create_date}

            userFrom = message.from_user
            resultFrom = {"username":userFrom.student_id,
                    "name":userFrom.student_name, "user_id":userFrom.student_id,
                    "created_at":userFrom.create_date}
            result.append({"created_at": message.create_date, "to": resultTo,
                "_from": resultFrom, "content": message.message_content,
                "message_id": message.message_id})
    else:
        # return all user.messages_recv
        for message in it.chain(user.messages_recv, user.messages_sent):
            # This is VERY ugly
            userTo = message.to_user
            resultTo = {"username":userTo.student_id,
                    "name":userTo.student_name, "user_id":userTo.student_id,
                    "created_at":userTo.create_date}

            userFrom = message.from_user
            resultFrom = {"username":userFrom.student_id,
                    "name":userFrom.student_name, "user_id":userFrom.student_id,
                    "created_at":userFrom.create_date}
            result.append({"created_at": message.create_date, "to": resultTo,
                "_from": resultFrom, "content": message.message_content,
                "message_id": message.message_id})
    
    return flask.json.jsonify(result), 200

@api_register.route('/message/<int:messageID>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{ 'in': 'path', 'name': 'messageID',
        'type': 'int',
        'required': 'true'
    },
    {
        'in': 'header',
        'name': 'Authorization',
        'type': 'string',
        'required': 'false'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual message item',
            'schema': models.MessageModel.schema()
        },
        404: {
            'description': 'messageID was not found',
        },
        400: {
            'description': 'Invalid Authorization',
        }
    }
})
def message_id_get(messageID: int):
    message = dbs.Umessage.query.filter_by(message_id=messageID).first()

    # the order in which this happens gives attackers info
    if not message:
        return "messageID was not found", 404

    studentID = request.headers.get("x-uq-user", None)
    if not studentID or (message.from_user_id != studentID and
            message.to_user_id != studentID):
        return "Invalid Authorization", 400

    userTo = dbs.UserDB.query.filter_by(student_id=message.to_user_id).first()
    resultTo = models.UserModel(username=userTo.student_id,
            name=userTo.student_name, user_id=userTo.student_id,
            created_at=userTo.create_date)

    userFrom = dbs.UserDB.query.filter_by(student_id=message.from_user_id).first()
    resultFrom = models.UserModel(username=userFrom.student_id,
            name=userFrom.student_name, user_id=userFrom.student_id,
            created_at=userFrom.create_date)

    result = models.MessageModel(created_at=message.create_date, to=userTo,
            _from=userFrom, content=message.message_content,
            message_id=message.message_id)

    return models.MessageModel.schema()().jsonify(result), 200


@api_register.route('/message/user/<string:userID>', methods=["POST"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'string',
        'required': 'true'
        },
        swag_param(PARAM_IN.QUERY, "content", str)
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Send a message to a user',
            'schema': models.MessageModel.schema()
        },
        400: {
            'description': 'Missing username',
        }
    }
})
def message_id_send(userID: str):
    studentID = request.headers.get("x-uq-user", None)
    if not studentID:
        return "Missing username", 400

    if dbs.UserDB.query.filter_by(student_id=studentID).scalar() is None:
        return "Missing username", 400

    row = dbs.Umessage(message_content=request.args.get("content",None),
            from_user_id=studentID, to_user_id=userID,
            create_date=datetime.now())

    dbs.db.session.add(row)
    dbs.db.session.commit()
    # retrieve from messagedb
    message = dbs.Umessage.query.filter_by(message_id=row.message_id).first()

    userTo = dbs.UserDB.query.filter_by(student_id=message.to_user_id).first()
    resultTo = models.UserModel(username=userTo.student_id,
            name=userTo.student_name, user_id=userTo.student_id,
            created_at=userTo.create_date)

    userFrom = dbs.UserDB.query.filter_by(student_id=message.from_user_id).first()
    resultFrom = models.UserModel(username=userFrom.student_id,
            name=userFrom.student_name, user_id=userFrom.student_id,
            created_at=userFrom.create_date)

    result = models.MessageModel(created_at=message.create_date, to=resultTo,
            _from=resultFrom, content=message.message_content,
            message_id=message.message_id)
    return models.MessageModel.schema()().jsonify(result), 200

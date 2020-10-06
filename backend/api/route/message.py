from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
import api.model as models
import api.db as dbs
from .api_register import api_register

from flask import request
from utils.route_utils import swag_param, PARAM_IN

@api_register.route('/messages/<string:userID>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'messageID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'List messages',
            'schema': models.MessageModel.schema()
        }
    }
})
def message_user_list(userID: int):
    result = None  # TODO FIX
    return models.MessageModel.schema()().jsonify(result), 200

@api_register.route('/message/<int:messageID>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'messageID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual message item',
            'schema': models.MessageModel.schema()
        }
    }
})
def message_id_get(messageID: int):
    result = None  # TODO FIX
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
        }
    }
})
def message_id_send(userID: str):
    row = dbs.Umessage(message_content=request.args["content"],
            from_user_id=request.headers["x-uq-user"], to_user_id=userID,
            create_date=datetime.now())

    dbs.db.session.add(row)
    dbs.db.session.commit()
    # retrieve from messagedb
    message = dbs.Umessage.query.filter_by(message_id=row.message_id).first()
    print(message.to_user_id)

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

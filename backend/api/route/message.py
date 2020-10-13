from .api_register import api_register
from .user import create_user_model

from http import HTTPStatus
from datetime import datetime
from flasgger import swag_from
from flask import request
from flask_praetorian import auth_required, current_user

import flask

from api.model import MessageModel, UserModel
from api.db import db, Message, User 
from utils.route_utils import swag_param, PARAM_IN

@api_register.route('/messages/<string:user_id>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'user_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'List messages',
            'schema': MessageModel.schema()
        },
        404: {
            'description': 'user_id not found',
        }
    }
})
@auth_required
def get_messages(user_id: str):
    user = current_user()

    sent = user.messages_sent.filter(Message.to_user_id == user_id)
    recv = user.messages_recv.filter(Message.from_user_id == user_id)
    messages = sent.union(recv).order_by(Message.created_at.desc())

    result = [create_message_model(m) for m in messages]
    
    return MessageModel.schema()().jsonify(result, many=True), HTTPStatus.OK

@api_register.route('/message/<int:message_id>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{ 'in': 'path', 'name': 'message_id',
        'type': 'int',
        'required': 'true'
    },
    {
        'in': 'header',
        'name': 'x-uq-user',
        'type': 'string',
        'required': 'false'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual message item',
            'schema': MessageModel.schema()
        },
        404: {
            'description': 'message_id was not found',
        },
        400: {
            'description': 'Invalid x-uq-user',
        }
    }
})
@auth_required
def get_message(message_id: int):
    user = current_user()

    message = Message.query.get(message_id)

    if not message:
        return "Message not found", HTTPStatus.NOT_FOUND

    if message.from_user_id != user.id and message.to_user_id != user.id:
        return "Message not found", HTTPStatus.NOT_FOUND

    result = create_message_model(message)

    return MessageModel.schema()().jsonify(result), HTTPStatus.OK


@api_register.route('/message/user/<string:user_id>', methods=["POST"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'user_id',
        'type': 'string',
        'required': 'true'
        },
        swag_param(PARAM_IN.QUERY, "content", str)
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Send a message to a user',
            'schema': MessageModel.schema()
        },
        400: {
            'description': 'Missing username',
        }
    }
})
@auth_required
def send_message(user_id: str):
    user = current_user()
    content = request.args.get("content")

    row = Message(content=request.args.get("content",None),
                  from_user_id=user.id, 
                  to_user_id=user_id,
                  created_at=datetime.now())

    db.session.add(row)
    db.session.commit()

    # retrieve from messagedb
    message = Message.query.get(row.id)

    result = create_message_model(message)

    return MessageModel.schema()().jsonify(result), HTTPStatus.OK

def create_message_model(message: Message) -> MessageModel:
    user_to = User.query.get(message.from_user_id)
    user_from = User.query.get(message.to_user_id)

    result = MessageModel(created_at=message.created_at,
                          to=create_user_model(user_to),
                          _from=create_user_model(user_from),
                          content=message.content,
                          message_id=message.id)
    return result


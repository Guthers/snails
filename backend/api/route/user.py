from .api_register import api_register

from datetime import datetime
from http import HTTPStatus
from flask import request, jsonify
from flasgger import swag_from

import json

from api.db import db, User
from api.model import UserModel
from api.guard import guard


@api_register.route('/user/login', methods=["POST"])
def login():
    username = request.get_json(force=True).get('username', None)
    password = request.get_json(force=True).get('password', None)
    user = guard.authenticate(username, password)

    result = {'access_token': guard.encode_jwt_token(user)}

    return jsonify(result), HTTPStatus.OK


@api_register.route('/user/register', methods=["POST"])
def register():
    username = request.get_json(force=True).get('username', None)
    password = request.get_json(force=True).get('password', None)

    exists = User.lookup(username) is not None

    if exists:
        return "", HTTPStatus.NOT_FOUND
    user = User(username=username,
                password=guard.hash_password(password),
                created_at=datetime.now())
    db.session.add(user)
    db.session.commit()

    user = guard.authenticate(username, password)

    result = {'access_token': guard.encode_jwt_token(user)}

    return jsonify(result), HTTPStatus.OK


@api_register.route('/user/<string:username>', methods=["GET"])
@swag_from({
    'tags': ['User'],
    'parameters': [{
        'in': 'path',
        'name': 'user_id',
        'type': 'string',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get user info',
            'schema': UserModel.schema()
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "user_id not found"'
        }
    }
})
def get_user(username: str):
    user = User.lookup(username)

    if user is None:
        return "User not found", HTTPStatus.NOT_FOUND

    result = create_user_model(user)

    return result.schema()().jsonify(result), HTTPStatus.OK


def create_user_model(user: User) -> UserModel:
    result = UserModel(created_at=user.created_at,
                       username=user.username,
                       name=user.name,
                       user_id=user.id)
    return result
from .api_register import api_register

from datetime import datetime
from http import HTTPStatus
from flask import request
from flasgger import swag_from

import json

from api.db import db, User
from api.model import UserModel
from utils.api_utils import safe_fail

@api_register.route('/user', methods=["POST"])
@swag_from({
    'tags': ['User'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Creates a user',
            'schema': UserModel.schema()
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "Invalid username or name" or "Failed tocommit to database"'
        }
    }
})
def create_user():
    student_id = request.headers.get("x-uq-user", None)
    userInfo = json.loads(request.headers["x-kvd-payload"])

    if not student_id:
        return "Missing username", HTTPStatus.BAD_REQUEST

    # check if student is in userdb
    if User.query.get(student_id):
        return "User already exists", HTTPStatus.BAD_REQUEST

    db.session.add(User(id=student_id,
                        name=userInfo["name"], 
                        created_at=datetime.now()))
    db.session.commit()

    # retrieve from userdb
    user = User.query.get(student_id)
    if user is None:
        return "Failed to commit to database", HTTPStatus.NOT_FOUND

    result = create_user_model(user)

    return result.schema()().jsonify(result), HTTPStatus.OK


@api_register.route('/user/<string:user_id>', methods=["GET"])
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
def get_user(user_id: str):
    user = User.query.get(user_id)

    if user is None:
        return "User not found", HTTPStatus.NOT_FOUND

    result = create_user_model(user)

    return result.schema()().jsonify(result), HTTPStatus.OK


def create_user_model(user: User) -> UserModel:
    result = UserModel(created_at=user.created_at,
                       username=user.id,
                       name=user.name,
                       user_id=user.id)
    return result
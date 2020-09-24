import json
from datetime import datetime
from http import HTTPStatus
from flask import request
from utils.api_utils import safe_fail
from flasgger import swag_from
import api.model as models
import api.db as dbs
from .api_register import api_register

@api_register.route('/user', methods=["POST"])
@swag_from({
    'tags': ['User'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Creates a user',
            'schema': models.UserModel.schema()
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "Invalid username or name" or "Failed to
            commit to database"'
        }
    }
})
def user():
    studentID = request.headers["x-uq-user"]
    userInfo = json.loads(request.headers["x-kvd-payload"])
    # check if student is in userdb
    if dbs.UserDB.query.filter_by(studentID=studentID).scalar() is not None:
        return "Invalid username or name", 400

    dbs.session.add(dbs.UserDB(studentID = studentID, studentname =
        userInfo["name"], createDate = datetime.now()))
    dbs.session.commti()

    # retrieve from userdb
    user = dbs.UserDB.query.filter_by(studentID=studentID).first()

    if user is None:
        return "Failed to commit to database", 400

    result = models.UserModel(username = user.studentID, name =
            user.studentName, user_id = user.studentID, created_at =
            user.createDate)
    return models.UserModel.schema()().jsonify(result), 200


@api_register.route('/user/<str:userID>', methods=["GET"])
@swag_from({
    'tags': ['User'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'str',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get user info',
            'schema': models.UserModel.schema()
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "userID not found"'
        }
    }
})
def user_id(userID: str):
    # retrieve from userdb
    user = dbs.UserDB.query.filter_by(studentID=userID).first()

    if user is None:
        return "userID not found", 400

    result = models.UserModel(username = user.studentID, name =
            user.studentName, user_id = user.studentID, created_at =
            user.createDate)
    return result.schema()().jsonify(result), 200


@api_register.route('/user/<int:userID>/messages', methods=["GET"])
@swag_from({
    'tags': ['User'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a users messages',
            'schema': models.MessageModel.schema()
        }
    }
})
@safe_fail
def user_message(userID: int):
    result = models.MessageModel()
    return models.MessageModel.schema()().dump(result), 200

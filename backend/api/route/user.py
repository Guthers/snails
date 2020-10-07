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
            'description': 'Returns "Invalid username or name" or "Failed tocommit to database"'
        }
    }
})
def user():
    studentID = request.headers.get("x-uq-user", None)
    if not studentID:
        return "Missing username", 400
    userInfo = json.loads(request.headers["x-kvd-payload"])
    # check if student is in userdb
    if dbs.UserDB.query.filter_by(student_id=studentID).scalar() is not None:
        return "Invalid username or name", 400

    dbs.db.session.add(dbs.UserDB(student_id=studentID,
        student_name=userInfo["name"], create_date=datetime.now()))
    dbs.db.session.commit()

    # retrieve from userdb
    user = dbs.UserDB.query.filter_by(student_id=studentID).first()

    if user is None:
        return "Failed to commit to database", 400

    result = models.UserModel(username=user.student_id, name=user.student_name,
            user_id=user.student_id, created_at=user.create_date)
    return models.UserModel.schema()().jsonify(result), 200


@api_register.route('/user/<string:userID>', methods=["GET"])
@swag_from({
    'tags': ['User'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'string',
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
    user = dbs.UserDB.query.filter_by(student_id=userID).first()

    if user is None:
        return "userID not found", 400

    result = models.UserModel(username=user.student_id, name=user.student_name,
            user_id=user.student_id, created_at=user.create_date)
    return result.schema()().jsonify(result), 200


# Was this part of the spec?
# Will implement if needed but for now silenced
#@api_register.route('/user/<int:userID>/messages', methods=["GET"])
#@swag_from({
#    'tags': ['User'],
#    'parameters': [{
#        'in': 'path',
#        'name': 'userID',
#        'type': 'int',
#        'required': 'true'
#    }],
#    'responses': {
#        HTTPStatus.OK.value: {
#            'description': 'Get a users messages',
#            'schema': models.MessageModel.schema()
#        }
#    }
#})
#@safe_fail
#def user_message(userID: int):
#    result = models.MessageModel()
#    return models.MessageModel.schema()().dump(result), 200

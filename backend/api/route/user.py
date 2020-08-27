from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/user', methods=["POST"])
@swag_from({
    'tags': ['User'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This actually hurts',
            'schema': models.UserModel.schema()
        }
    }
})
def user():
    result = models.UserModel()
    return models.UserModel.schema().dump(result), 200


@api_register.route('/user/<int:userID>', methods=["GET"])
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
            'description': 'This actually hurts',
            'schema': models.UserModel.schema()
        }
    }
})
def user_id(userID: int):
    from datetime import datetime
    result = models.UserModel(datetime.now(), "Foobar", "barson", userID)
    return models.UserModel.schema().dump(result), 200


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
def user_message(userId: int):
    result = models.MessageModel()
    return models.MessageModel.schema().dump(result), 200

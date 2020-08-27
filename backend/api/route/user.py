from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/user')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This actually hurts',
            'schema': models.UserModel.UserSchema
        }
    }
})
def user():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = models.UserModel()
    return models.UserModel.UserSchema().dump(result), 200


@api_register.route('/user/<int:userID>')
@swag_from({
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This actually hurts',
            'schema': models.UserModel.UserSchema
        }
    }
})
def user_id(userID: int):
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    from datetime import datetime
    result = models.UserModel(datetime.now(), "Foobar", "barson", userID)
    return models.UserModel.UserSchema().dump(result), 200

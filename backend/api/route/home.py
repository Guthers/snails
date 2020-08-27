from http import HTTPStatus
from flasgger import swag_from
from api.model.welcome import WelcomeModel
from .api_register import api_register


@api_register.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeModel.WelcomeSchema
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = WelcomeModel()
    return WelcomeModel.WelcomeSchema().dump(result), 200

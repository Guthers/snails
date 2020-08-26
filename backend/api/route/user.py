from http import HTTPStatus
from flasgger import swag_from
import api.model as models
import api.schema as schemas
from .api_register import api_register


@api_register.route('/user')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This actually hurts',
            'schema': schemas.UserSchema
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
    return schemas.UserSchema().dump(result), 200

from http import HTTPStatus
from flasgger import swag_from
import api.model as models
import api.schema as schemas
from .api_register import api_register


@api_register.route('/weather')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This is actually weather',
            'schema': schemas.WeatherSchema
        }
    }
})
def weather():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = models.WeatherModel()
    return schemas.WeatherSchema().dump(result), 200

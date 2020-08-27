from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/weather')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'This is actually weather',
            'schema': models.WeatherModel.WeatherSchema
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
    return models.WeatherModel.WeatherSchema().dump(result), 200
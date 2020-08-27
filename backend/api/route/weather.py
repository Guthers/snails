from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/weather', methods=["GET"])
@swag_from({
    'tags': ['Weather'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the current weather information',
            'schema': models.WeatherModel.schema()
        }
    }
})
def weather():
    result = models.WeatherModel()
    return models.WeatherModel.schema().dump(result), 200

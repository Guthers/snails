from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/maps', methods=["GET"])
@swag_from({
    'tags': ['Maps'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a map link',
            'schema': models.MapModel.schema()
        }
    }
})
def maps():
    result = models.MapModel()
    return models.MapModel.schema().dump(result), 200


@api_register.route('/maps/<int:mapsID>', methods=["GET"])
@swag_from({
    'tags': ['Maps'],
    'parameters': [{
        'in': 'path',
        'name': 'mapsID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual maps item',
            'schema': models.MapModel.schema()
        }
    }
})
def maps_id(mapsID: int):
    result = None  # TODO FIX
    return models.MapModel.schema().dump(result), 200

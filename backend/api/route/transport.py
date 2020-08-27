from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/transport', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport():
    result = models.VehicleModel()
    return models.VehicleModel.schema()().jsonify(result), 200


@api_register.route('/transport/<int:transportID>', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'parameters': [{
        'in': 'path',
        'name': 'transportID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual transport item',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport_id(transportID: int):
    result = None  # TODO FIX
    return models.VehicleModel.schema()().jsonify(result), 200

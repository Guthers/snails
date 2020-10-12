from .api_register import api_register

from http import HTTPStatus
from flasgger import swag_from

from api.model import VehicleModel

@api_register.route('/transport', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': VehicleModel.schema()
        }
    }
})
def transport():
    result = VehicleModel()
    return VehicleModel.schema()().jsonify(result), HTTPStatus.OK


@api_register.route('/transport/<int:transport_id>', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'parameters': [{
        'in': 'path',
        'name': 'transport_id',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual transport item',
            'schema': VehicleModel.schema()
        }
    }
})
def transport_id(transport_id: int):
    result = None  # TODO FIX
    return VehicleModel.schema()().jsonify(result), HTTPStatus.OK

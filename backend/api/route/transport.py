from .api_register import api_register

from http import HTTPStatus
from flasgger import swag_from

from api.model import VehicleModel
from utils.route_utils import swag_param, PARAM, VALUE

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
    'parameters': [
        swag_param(PARAM.PATH, "transport_id", VALUE.INTEGER)
    ],
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

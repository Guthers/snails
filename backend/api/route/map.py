from .api_register import api_register

from http import HTTPStatus
from flasgger import swag_from
from flask import request

from api.model import MapModel
from utils.route_utils import swag_param, PARAM, VALUE


@api_register.route('/maps', methods=["GET"])
@swag_from({
    'tags': ['Maps'],
    'parameters': [
        swag_param(PARAM.QUERY, "lat", VALUE.STRING),
        swag_param(PARAM.QUERY, "lng", VALUE.STRING)],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a map link',
            'schema': MapModel.schema()
        }
    }
})
def maps():
    result = MapModel(request.args["lat"], request.args["lng"])
    return MapModel.schema()().jsonify(result), HTTPStatus.OK


@api_register.route('/maps/board', methods=["GET"])
@swag_from({
    'tags': ['Maps'],
    'parameters': [
        swag_param(PARAM.QUERY, "board_id", VALUE.STRING),
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual maps item',
            'schema': MapModel.schema()
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "Error: Bad Request"'
        }
    }
})
def maps_id():
    # assuming dict with tuple entries (lat, long)
    boards = {69: (153.013171, -27.497083), 420: (153.014641, -27.499610)}
    board_id = request.args["board_id"]
    board_id = int(board_id) if board_id.isdigit() else -1

    if board_id not in boards:
        return "Error: Bad Request", HTTPStatus.BAD_REQUEST

    result = MapModel(*boards[board_id])
    return MapModel.schema()().jsonify(result), HTTPStatus.OK

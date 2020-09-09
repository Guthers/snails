from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register
from flask import request


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
    result = models.MapModel(request.args["lat"], request.args["lng"])
    return models.MapModel.schema()().jsonify(result), 200


@api_register.route('/maps/board', methods=["GET"])
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
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Returns "Error: Bad Request"'
        }
    }
})
def maps_id():
    # assuming dict with tuple entries (lat, long)
    boards = {69: (153.013171, -27.497083), 420: (153.014641, -27.499610)}
    boardID = request.args["id"]
    boardID = int(boardID) if boardID.isdigit() else -1

    if boardID not in boards:
        return "Error: Bad Request", 400

    result = models.MapModel(*boards[boardID])
    return models.MapModel.schema()().jsonify(result), 200

from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/message/<int:messageID>', methods=["GET"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'messageID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual message item',
            'schema': models.MessageModel.schema()
        }
    }
})
def message_id_get(messageID: int):
    result = None  # TODO FIX
    return models.MessageModelschema()().jsonify(result), 200


@api_register.route('/message/<int:userID>', methods=["POST"])
@swag_from({
    'tags': ['Message'],
    'parameters': [{
        'in': 'path',
        'name': 'userID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Send a message to a user',
            'schema': models.MessageModel.schema()
        }
    }
})
def message_id_send(userID: int):
    result = None  # TODO FIX
    return models.MessageModelschema()().jsonify(result), 200

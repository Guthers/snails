from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/entry', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Creates an entry',
            'schema': models.EntryModel.schema()
        }
    }
})
def entry():
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200


@api_register.route('/entry/<int:entryID>', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the entry by the specified id',
            'schema': models.EntryModel.schema()
        }
    }
})
def entry_id(entryID: int):
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200


@api_register.route('/entry/<int:entryID>/replies', methods=["GET"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the entry specified by the id\'s replies',
            'schema': models.EntryModel.schema()
        }
    }
})
def entry_id_replies(entryID: int):
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200  # TODO Schema is wrong


@api_register.route('/entry/like/<int:entryID>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Like the specified entry',
            'schema': models.EntryModel.schema()
        }
    }
})
def like_entry(entryID: int):
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200  # TODO Schema is wrong


@api_register.route('/entry/unlike/<int:entryID>', methods=["POST"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Unlike the specified entry',
            'schema': models.EntryModel.schema()
        }
    }
})
def unlike_entry(entryID: int):
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200  # TODO Schema is wrong


@api_register.route('/entry/<int:entryID>', methods=["DELETE"])
@swag_from({
    'tags': ['Entry'],
    'parameters': [{
        'in': 'path',
        'name': 'entryID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Delete the entry by the specified id',
            'schema': models.EntryModel.schema()
        }
    }
})
def delete_entry(entryID: int):
    result = models.EntryModel()
    return models.EntryModel.schema().dump(result), 200  # TODO Schema is wrong

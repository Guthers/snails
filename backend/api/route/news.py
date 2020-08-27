from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register


@api_register.route('/news', methods=["GET"])
@swag_from({
    'tags': ['News'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of news items',
            'schema': models.NewsModel.schema()
        }
    }
})
def news():
    result = models.NewsModel()
    return models.NewsModel.schema()().jsonify(result), 200


@api_register.route('/news/<int:newsID>', methods=["GET"])
@swag_from({
    'tags': ['News'],
    'parameters': [{
        'in': 'path',
        'name': 'newsID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual news item',
            'schema': models.NewsModel.schema()
        }
    }
})
def news_id(newsID: int):
    result = None  # TODO FIX
    return models.NewsModel.schema()().jsonify(result), 200

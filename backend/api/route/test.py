import json
from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register
from flask import request
from api.db import db


@api_register.route('/user_info', methods=["GET"])
@swag_from({
    'tags': ['Test'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get the user test info'
            # 'schema': models.UserModel.schema()
        }
    }
})
def user_info():
    userjson = request.headers['x-kvd-payload']
    user = json.loads(userjson)
    return user

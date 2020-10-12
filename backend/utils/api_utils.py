from http import HTTPStatus
import functools
from api.model.exception import ExceptionModel


def safe_fail(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return ExceptionModel.schema()().jsonify(ExceptionModel(f"Unexpected exception enocuntered: {e}")), HTTPStatus.INTERNAL_SERVER_ERROR
    return decorated_function

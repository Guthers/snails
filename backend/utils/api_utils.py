import functools
from api.model.exception import ExceptionModel


def safe_fail(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return ExceptionModel.schema()().jsonify(ExceptionModel(f"Unexpected exception enocuntered: {e}")), 500
    return decorated_function

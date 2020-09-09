from enum import Enum


class PARAM_IN(Enum):
    PATH = "path"
    QUERY = "query"


def swag_param(param_in: PARAM_IN, name: str, type: type, required=True):
    return {
        'in': param_in.value,
        'name': name,
        'type': type.__name__,
        'required': str(required).lower()
    }

from enum import Enum


class PARAM(Enum):
    PATH = "path"
    QUERY = "query"
    HEADER = "header"
    BODY = "body"
    DATA = "formData"

class VALUE(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    ARRAY = "array"


def swag_param(param: PARAM, name: str, type_: VALUE, required=True):
    return {
        'in': param.value,
        'name': name,
        'type': type_.value,
        'required': required
    }

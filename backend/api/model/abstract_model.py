from flask_marshmallow import Schema
import marshmallow as ma
from datetime import datetime
from inspect import signature


class AbstractModel():
    """ Adds additional functionality to models
        - Namely auto-generation of schemas
    """

    type_mapper = {
        str: ma.fields.Str(),
        int: ma.fields.Int(),
        float: ma.fields.Float(),
        datetime: ma.fields.DateTime()
    }

    @classmethod
    def schema(calling_class):
        schema_name = calling_class.__name__ + "Schema"

        params = {}

        init_params = signature(calling_class.__init__)

        for param in init_params.parameters:
            if param != "self":
                type_annotation = init_params.parameters[param].annotation

                print(f"param: {param} has type {type_annotation}")

                if type_annotation is None:
                    type_annotation = str
                params[param] = AbstractModel.type_mapper[type_annotation]

        SubClass = type(schema_name, (Schema,), params)
        return SubClass

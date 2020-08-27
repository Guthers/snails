from __future__ import annotations
from flask_marshmallow import Schema
import marshmallow as ma
from datetime import datetime
from inspect import signature
from typing import Type


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
    def schema(cls: Type[AbstractModel]) -> Schema:
        """
            Automatically generates the swagger scheam for classes which inherit
            the abstract class. It uses the classes __init__ function, combined
            with the type annotations.

            If no type annotation is supplied, it is assumed string. If it is
            provided then it is checked against the AbstractModel.type_mapper.
            This will throw a KeyError. Which is okay, as this function is run
            when the api is being registered, which happens on startup (fail
            fast, fail often, fail hard).

            :param cls: The subclass which inherits AbstractModel.
            :type cls: Subclass of AbstractModel

        """
        schema_name = cls.__name__
        if "Model" in schema_name:
            schema_name = cls.__name__.replace("Model", "Schema")
        else:
            schema_name += "Schema"

        params = {}

        init_params = signature(cls.__init__)

        for param in init_params.parameters:
            if param != "self":
                type_annotation = init_params.parameters[param].annotation

                print(f"param: {param} has type {type_annotation}")

                if type_annotation is None:
                    type_annotation = str
                params[param] = AbstractModel.type_mapper[type_annotation]

        SubClass = type(schema_name, (Schema,), params)
        return SubClass

from utils.class_utils import get_abstract_subclasses
from flask_marshmallow import Schema
import marshmallow as ma
import typing


class AbstractModel():
    """ Adds additional functionality to models
        - Namely auto-generation of schemas
    """
    @classmethod
    def schema(cls) -> Schema:
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
        # Get the initial params for the init function
        init_params = typing.get_type_hints(cls.__init__)

        # The paramaters after they have being turned into the marshmellow types
        params = {}
        for param in init_params:
            if param != "self":
                type_annotation = init_params[param]
                resolved_type = AbstractModel.resolve_typing(type_annotation)
                params[param] = resolved_type

        SubClass = type(schema_name, (Schema,), params)
        return SubClass

    @staticmethod
    def resolve_typing(type_annotation):
        if type_annotation is None:
            return ma.fields.Str()
        else:
            # It will be a type, almost always a union
            localised_annotation = str
            type_annotation_base = typing.get_origin(type_annotation)
            type_annotation_args = typing.get_args(type_annotation)
            if type_annotation_base == typing.Union:
                a, b = type_annotation_args
                if a is None:
                    localised_annotation = b
                else:
                    localised_annotation = a
            else:
                if type_annotation_base is not None:
                    localised_annotation = type_annotation_base
                else:
                    localised_annotation = type_annotation

            if typing.get_origin(localised_annotation) == list:
                list_type = typing.get_args(localised_annotation)[0]
                return ma.fields.List(AbstractModel.resolve_typing(list_type))

        # Check if type is actually a subclass as well
        if localised_annotation not in ma.Schema.TYPE_MAPPING:
            sub_classes = get_abstract_subclasses([AbstractModel])
            if localised_annotation in sub_classes:
                return ma.fields.Nested(localised_annotation.schema())

        # TODO Check for list as well
        return ma.Schema.TYPE_MAPPING[localised_annotation]()

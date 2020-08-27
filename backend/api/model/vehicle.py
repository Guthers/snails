from flask_marshmallow import Schema
import marshmallow as ma


class VehicleModel:
    def __init__(self, eta: int = None, name: str = None, code: str = None):
        """Vehicle - a model defined in Swagger

        :param eta: The eta of this Vehicle.  # noqa: E501
        :type eta: int
        :param name: The name of this Vehicle.  # noqa: E501
        :type name: str
        :param code: The code of this Vehicle.  # noqa: E501
        :type code: str
        """
        self.eta = eta
        self.name = name
        self.code = code

    class VehicleSchema(Schema):
        eta = ma.fields.Integer()
        name = ma.fields.Str()
        code = ma.fields.Str()

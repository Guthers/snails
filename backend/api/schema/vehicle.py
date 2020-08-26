from flask_marshmallow import Schema
import marshmallow as ma


class VehicleSchema(Schema):
    eta = ma.fields.Integer()
    name = ma.fields.Str()
    code = ma.fields.Str()

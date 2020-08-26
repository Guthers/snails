from flask_marshmallow import Schema
import marshmallow as ma


class WeatherSchema(Schema):
    created_at = ma.fields.DateTime()
    current_temperature = ma.fields.Integer()
    precipitation = ma.fields.Float()
    humidity = ma.fields.Float()
    uv_index = ma.fields.Integer()
    conditions = ma.fields.Str()
    max_temperature = ma.fields.Integer()
    min_temperature = ma.fields.Integer()

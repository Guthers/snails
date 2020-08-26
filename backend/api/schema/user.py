from flask_marshmallow import Schema
import marshmallow as ma


class UserSchema(Schema):
    created_at = ma.fields.DateTime()
    username = ma.fields.Str()
    name = ma.fields.Str()
    user_id = ma.fields.Str()

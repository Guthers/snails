from flask_marshmallow import Schema
import marshmallow as ma


class MessageSchema(Schema):
    created_at = ma.fields.DateTime()
    to = ma.fields.Str()
    _from = ma.fields.Str()
    content = ma.fields.Str()
    message_id = ma.fields.Str()

from flask_marshmallow import Schema
import marshmallow as ma


class EntrySchema(Schema):
    created_at = ma.fields.DateTime()
    reply_to = ma.fields.Str()
    content = ma.fields.Str()
    liked_by = ma.fields.List(ma.fields.Str())
    replies = ma.fields.List(ma.fields.Str())
    author = ma.fields.Str()
    entry_id = ma.fields.Str()

from flask_marshmallow import Schema
import marshmallow as ma


class NewsSchema(Schema):
    created_at = ma.fields.DateTime()
    url = ma.fields.URL()
    content = ma.fields.Str()
    image_url = ma.fields.URL()
    news_id = ma.fields.Str()
    title = ma.fields.Str()

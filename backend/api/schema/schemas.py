from flask_marshmallow import Schema
import marshmallow as ma

# Should be noted that created_at is a str instead of a date and time. I only
# did this because I don't know how to use datetime with marshmallow
# not sure how to use marshmallow for constraints i.e. EntrySchema->author is
# just a string NOT a user

class NewsSchema(Schema):
    created_at = ma.fields.DateTime()
    url = ma.fields.URL()
    content = ma.fields.Str()
    image_url = ma.fields.URL()
    news_id = ma.fields.Str()
    title = ma.fields.Str()
    
class WeatherSchema(Schema):
    created_at = ma.fields.DateTime()
    current_temperature = ma.fields.Integer()
    precipitation = ma.fields.Float()
    humidity = ma.fields.Float()
    uv_index = ma.fields.Integer()
    conditions = ma.fields.Str()
    max_temperature = ma.fields.Integer()
    min_temperature = ma.fields.Integer()

class UserSchema(Schema):
    created_at = ma.fields.DateTime()
    username = ma.fields.Str()
    name = ma.fields.Str()
    user_id = ma.fields.Str()

class EntrySchema(Schema):
    created_at = ma.fields.DateTime()
    reply_to = ma.fields.Str()
    content = ma.fields.Str()
    liked_by = ma.fields.List(ma.fields.Str())
    replies = ma.fields.List(ma.fields.Str())
    author = ma.fields.Str()
    entry_id = ma.fields.Str()

class VehicleSchema(Schema):
    eta = ma.fields.Integer()
    name = ma.fields.Str()
    code = ma.fields.Str()

class MessageSchema(Schema):
    created_at = ma.fields.DateTime()
    to = ma.fields.Str()
    _from = ma.fields.Str()
    content = ma.fields.Str()
    message_id = ma.fields.Str()

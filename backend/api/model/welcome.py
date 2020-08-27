from flask_marshmallow import Schema
import marshmallow as ma


class WelcomeModel:
    def __init__(self):
        self.message = "Hello World!"

    class WelcomeSchema(Schema):
        class Meta:
            # Fields to expose
            fields = ["message"]

        message = ma.fields.Str()

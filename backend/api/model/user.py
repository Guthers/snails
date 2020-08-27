from datetime import datetime
from flask_marshmallow import Schema
import marshmallow as ma


class UserModel:
    def __init__(self, created_at: datetime = None, username: str = None,
                 name: str = None, user_id: int = None):
        """User - a model defined in Swagger

        :param created_at: The created_at of this User.  # noqa: E501
        :type created_at: UTCTime
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param id: The id of this User.  # noqa: E501
        :type id: int
        """
        self.created_at = created_at
        self.username = username
        self.name = name
        self.user_id = user_id

    class UserSchema(Schema):
        created_at = ma.fields.DateTime()
        username = ma.fields.Str()
        name = ma.fields.Str()
        user_id = ma.fields.Int()

from __future__ import annotations
from typing import List, TYPE_CHECKING
from flask_marshmallow import Schema
import marshmallow as ma


if TYPE_CHECKING:
    from api.model.user import UserModel


class EntryModel:
    def __init__(self, created_at: str = None, reply_to: str = None,
                 content: str = None, liked_by: List[UserModel] = None,
                 replies: List[str] = None, author: UserModel = None,
                 entry_id: str = None):
        """Entry - a model defined in Swagger

        :param created_at: The created_at of this Entry.  # noqa: E501
        :type created_at: UTCTime
        :param reply_to: The reply_to of this Entry.  # noqa: E501
        :type reply_to: str
        :param content: The content of this Entry.  # noqa: E501
        :type content: str
        :param liked_by: The liked_by of this Entry.  # noqa: E501
        :type liked_by: List[User]
        :param replies: The replies of this Entry.  # noqa: E501
        :type replies: List[str]
        :param author: The author of this Entry.  # noqa: E501
        :type author: User
        :param id: The id of this Entry.  # noqa: E501
        :type id: str
        """
        self.created_at = created_at
        self.reply_to = reply_to
        self.content = content
        self.liked_by = liked_by
        self.replies = replies
        self.author = author
        self.entry_id = entry_id

    class EntrySchema(Schema):
        created_at = ma.fields.DateTime()
        reply_to = ma.fields.Str()
        content = ma.fields.Str()
        liked_by = ma.fields.List(ma.fields.Str())
        replies = ma.fields.List(ma.fields.Str())
        author = ma.fields.Str()
        entry_id = ma.fields.Str()

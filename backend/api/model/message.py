from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from api.model.user import UserModel


class MessageModel:
    def __init__(self, created_at: str = None, to: UserModel = None,
                 _from: UserModel = None, content: str = None,
                 message_id: str = None):
        """Message - a model defined in Swagger

        :param created_at: The created_at of this Message.  # noqa: E501
        :type created_at: UTCTime
        :param to: The to of this Message.  # noqa: E501
        :type to: UserModel
        :param _from: The _from of this Message.  # noqa: E501
        :type _from: UserModel
        :param content: The content of this Message.  # noqa: E501
        :type content: str
        :param id: The id of this Message.  # noqa: E501
        :type id: str
        """
        self.created_at = created_at
        self.to = to
        self._from = _from
        self.content = content
        self.message_id = message_id

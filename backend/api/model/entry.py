from __future__ import annotations
from typing import List, TYPE_CHECKING
from .abstract_model import AbstractModel


if TYPE_CHECKING:
    from api.model.user import UserModel


class EntryModel(AbstractModel):
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

from .abstract_model import AbstractModel
from datetime import datetime


class NewsModel(AbstractModel):
    def __init__(self, created_at: datetime = None, url: str = None, content:
                 str = None, image_url: str = None, news_id: str = None, title: str = None):
        """News - a model defined in Swagger

        :param created_at: The created_at of this News.  # noqa: E501
        :type created_at: UTCTime
        :param url: The url of this News.  # noqa: E501
        :type url: str
        :param content: The content of this News.  # noqa: E501
        :type content: str
        :param image_url: The image_url of this News.  # noqa: E501
        :type image_url: str
        :param id: The id of this News.  # noqa: E501
        :type id: str
        :param title: The title of this News.  # noqa: E501
        :type title: str
        """
        self.created_at = created_at
        self.url = url
        self.content = content
        self.image_url = image_url
        self.news_id = news_id
        self.title = title

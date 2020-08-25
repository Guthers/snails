from typing import List, Dict

# Should be noted that created_at is a str instead of a date and time. I only
# did this because I don't know how to use datetime with marshmallow

class NewsModel:
    def __init__(self, created_at: str = None, url: str = None, content:
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

class WeatherModel:
    def __init__(self, created_at: str = None, current_temperature: int = None,
                 precipitation: float = None, humidity: float = None,
                 uv_index: int = None, conditions: str = None,
                 max_temperature: int = None, min_temperature: int = None):
        """Weather - a model defined in Swagger

        :param created_at: The created_at of this Weather.  # noqa: E501
        :type created_at: UTCTime
        :param current_temperature: The current_temperature of this Weather.  # noqa: E501
        :type current_temperature: int
        :param precipitation: The precipitation of this Weather.  # noqa: E501
        :type precipitation: float
        :param humidity: The humidity of this Weather.  # noqa: E501
        :type humidity: float
        :param uv_index: The uv_index of this Weather.  # noqa: E501
        :type uv_index: int
        :param conditions: The conditions of this Weather.  # noqa: E501
        :type conditions: WeatherCondition
        :param max_temperature: The max_temperature of this Weather.  # noqa: E501
        :type max_temperature: int
        :param min_temperature: The min_temperature of this Weather.  # noqa: E501
        :type min_temperature: int
        """
        self.created_at = created_at
        self.current_temperature = current_temperature
        self.precipitation = precipitation
        self.humidity = humidity
        self.uv_index = uv_index
        self.conditions = conditions
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature

class UserModel:
    def __init__(self, created_at: str = None, username: str = None,
                 name: str = None, user_id: str = None):
        """User - a model defined in Swagger

        :param created_at: The created_at of this User.  # noqa: E501
        :type created_at: UTCTime
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param id: The id of this User.  # noqa: E501
        :type id: str
        """
        self.created_at = created_at
        self.username = username
        self.name = name
        self.user_id = user_id

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

class VehicleModel:
    def __init__(self, eta: int = None, name: str = None, code: str = None):
        """Vehicle - a model defined in Swagger

        :param eta: The eta of this Vehicle.  # noqa: E501
        :type eta: int
        :param name: The name of this Vehicle.  # noqa: E501
        :type name: str
        :param code: The code of this Vehicle.  # noqa: E501
        :type code: str
        """
        self.eta = eta
        self.name = name
        self.code = code

class MessageModel:
    def __init__(self, created_at: str = None, to: UserModel = None,
                 _from: UserModel = None, content: str = None,
                 message_id: str=None):
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

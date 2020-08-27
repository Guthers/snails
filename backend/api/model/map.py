from .abstract_model import AbstractModel


class MapModel(AbstractModel):
    def __init__(self, url: str = None):
        """Map - a model defined in Swagger

        :param url: The maps url.  # noqa: E501
        :type content: str
        """
        self.url = url

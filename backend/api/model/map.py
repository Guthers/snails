from .abstract_model import AbstractModel


class MapModel(AbstractModel):
    def __init__(self, lat: float = 0, lng: float = 0):
        """Map - a model defined in Swagger

        :param url: The maps url.  # noqa: E501
        :type content: str
        """
        self.url = \
        "https://use.mazemap.com/embed.html#config=uq&v=1&zlevel=1&campuses=uq \
        &campusid=406&center=" + lat + "," + lng + "&zoom=18&utm_medium=iframe"

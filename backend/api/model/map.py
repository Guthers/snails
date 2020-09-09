from typing import overload
from .abstract_model import AbstractModel
from flask_marshmallow import Schema
import marshmallow as ma


class MapModel(AbstractModel):
    def __init__(self, lat: float = 0, lng: float = 0):
        """Map - a model defined in Swagger

        :param url: The maps url.  # noqa: E501
        :type content: str
        """
        self.url = \
            "https://use.mazemap.com/embed.html#config=uq&v=1&zlevel=1&campuses=uq&campusid=406&center=" + \
            str(lat) + "," + str(lng) + "&zoom=18&utm_medium=iframe"

    @classmethod
    def schema(cls) -> Schema:
        return type(cls.__name__.replace("Model", "Schema"), (Schema,), {"url": ma.Schema.TYPE_MAPPING[str]()})

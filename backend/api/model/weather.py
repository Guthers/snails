from flask_marshmallow import Schema
import marshmallow as ma


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

    class WeatherSchema(Schema):
        created_at = ma.fields.DateTime()
        current_temperature = ma.fields.Integer()
        precipitation = ma.fields.Float()
        humidity = ma.fields.Float()
        uv_index = ma.fields.Integer()
        conditions = ma.fields.Str()
        max_temperature = ma.fields.Integer()
        min_temperature = ma.fields.Integer()

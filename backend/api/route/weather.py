from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register

import datetime
import urllib.request
import xmltodict

from functools import lru_cache

# hardcoded since won't change
BOM_URL = 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDQ11295.xml'


@api_register.route('/weather', methods=["GET"])
@swag_from({
    'tags': ['Weather'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gets the current weather information',
            'schema': models.WeatherModel.schema()
        }
    }
})
def weather():
    result = get_bom()
    return get_weather(time() // 60 // 60)

#@lru_cache(max_size=2)
def get_weather(curtime):
    """Get the weather JSON file.

    curtime: current time in hours since the epoch
    """
    return models.WeatherModel.schema()().jsonify(result), 200

def get_bom() -> models.WeatherModel:
    # making a request to bom everytime is probably not okay. Save file maybe?
    with urllib.request.urlopen(BOM_URL) as req:
        # structure of bom xml sheet is hardcoded
        info = xmltodict.parse(req.read())["product"]["forecast"]["area"]

    # locate Brisbane
    info = next(filter(lambda i: i["@description"] == "Brisbane", info))
    # get first forecast period
    info = info["forecast-period"][0]

    created_at = datetime.datetime.strptime(info["@start-time-local"],
            "%Y-%m-%dT%H:%M:%S+10:00")

    current_temperature = int(next(filter(lambda i: i["@type"] ==
            "air_temperature_maximum", info["element"]))["#text"])

    precipitation = next(filter(lambda i: i["@type"] ==
            "precipitation_range", info["element"]), None)
    if precipitation:
        # VERY hardcoded but oh well. Should make flexible later
        precipitation = precipitation["#text"].split(' ')
        precipitation = (int(precipitation[0]) + int(precipitation[2]))/2

    # converts condition into PascalCase
    conditions = ''.join(x for x in next(filter(lambda i: i["@type"] ==
        "precis", info["text"]))["#text"][:-1].title() if not x.isspace())

    return models.WeatherModel(created_at=created_at,
            current_temperature=current_temperature,
            precipitation=precipitation, conditions=conditions)

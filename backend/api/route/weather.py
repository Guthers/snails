from http import HTTPStatus
from flasgger import swag_from
import api.model as models
from .api_register import api_register

import time
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
    return get_weather(time.time() // 60 // 60)

@lru_cache(maxsize=2)
def get_weather(curtime):
    """Get the weather JSON file.

    curtime: current time in hours since the epoch
    """
    return models.WeatherModel.schema()().jsonify(get_bom()), 200

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

    current_temperature = None
    prob_precipitation = None
    precipitation = None
    conditions = None
    if isinstance(info, list) or isinstance(info, dict):
        f = next(filter(lambda i: isinstance(i, dict) and i["@type"] ==
            "air_temperature_maximum", info), None)
        if f is not None:
            current_temperature = int(f["#text"])

        f = next(filter(lambda i: isinstance(i, dict) and i["@type"] ==
                "probability_of_precipitation", info["text"]), None)
        if f is not None:
            # VERY hardcoded but oh well. Should make flexible later
            prob_precipitation = int(f["#text"].strip("%"))

        f = next(filter(lambda i: isinstance(i, dict) and i["@type"] ==
                "precipitation_range", info), None)
        if f is not None:
            # VERY hardcoded but oh well. Should make flexible later
            precipitation = f["#text"].split(' ')
            precipitation = (int(precipitation[0]) + int(precipitation[2]))/2

        # converts condition into PascalCase
        f = next(filter(lambda i: isinstance(i, dict) and i["@type"] ==
            "precis", info["text"]), None)
        if f is not None:
            conditions = ''.join(x for x in f["#text"][:-1].title() if not x.isspace())

    return models.WeatherModel(created_at=created_at,
            current_temperature=current_temperature,
            prob_precipitation=prob_precipitation,
            precipitation=precipitation, conditions=conditions)

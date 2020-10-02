"""Get tha news"""

import json

from http import HTTPStatus
# from flasgger import swag_from
# import api.model as models
# from .api_register import api_register

from datetime import datetime
from time import time
import urllib.request
import xmltodict

from functools import lru_cache

UQNEWS_RSS_URL = 'http://www.uq.edu.au/news/rss/news_feed.xml'

# @api_register.route('/news', methods=["GET"])
# @swag_from({
#     'tags': ['News'],
#     'responses': {
#         HTTPStatus.OK.value: {
#             'description': 'Get a list of news items',
#             'schema': models.NewsModel.schema()
#         }
#     }
# })
def news():
    result = models.NewsModel()
    return models.NewsModel.schema()().jsonify(result), 200

def test_news():
    print(json.dumps(get_news(), sort_keys=True, indent=4))
    print(news_ids())
    print(json.dumps(news_id(news_ids()[3]), sort_keys=True, indent=4))

# @api_register.route('/news/<int:newsID>', methods=["GET"])
# @swag_from({
#     'tags': ['News'],
#     'parameters': [{
#         'in': 'path',
#         'name': 'newsID',
#         'type': 'int',
#         'required': 'true'
#     }],
#     'responses': {
#         HTTPStatus.OK.value: {
#             'description': 'Get an individual news item',
#             'schema': models.NewsModel.schema()
#         }
#     }
# })

def get_news():
    return refresh_news(time() // 60 // 60)

@lru_cache(maxsize=2)
def refresh_news(t):
    '''rss fails'''

    req = urllib.request.Request(UQNEWS_RSS_URL)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    with urllib.request.urlopen(req) as rss:
        items = xmltodict.parse(rss.read())["rss"]["channel"]["item"]


    for i in items:
        i["created_at"] = str(datetime.strptime(i.pop("pubDate"), "%a, %d %b %Y %H:%M:%S %z")) # TODO rm str
        i["url"] = i.pop("link")
        i["content"] = i.pop("description")
        i["image_url"] = None # TODO scrape it if desparate
        i["id"] = ''.join(c for c in i.pop("guid") if c.isdigit())
        del i["author"]

    return items

def news_ids():
    return [i["id"] for i in get_news()]
    
def news_id(newsID: int):
    results = [i for i in get_news() if i["id"] == str(newsID)]
    return results[0] if len(results) == 1 else None
    # return models.NewsModel.schema()().jsonify(result), 200

test_news()

"""Get tha news"""

from .api_register import api_register

from datetime import datetime
from flasgger import swag_from
from functools import lru_cache
from http import HTTPStatus
from time import time

import json
import flask
import urllib.request
import xmltodict

from api.model import NewsModel
from utils.route_utils import swag_param, PARAM, VALUE

UQNEWS_RSS_URL = 'http://www.uq.edu.au/news/rss/news_feed.xml'

@api_register.route('/news', methods=["GET"])
@swag_from({
    'tags': ['News'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of news items',
            'schema': {
                "type": "array",
                "items": NewsModel.schema()
            }
        }
    }
})
def news():
    res = refresh_news(time() // 60 // 60)
    #return json.dumps(res, default=str), HTTPStatus.OK
    # return NewsModel.schema()().jsonify(res), HTTPStatus.OK
    return flask.json.jsonify(res), HTTPStatus.OK

@api_register.route('/news/<string:news_id>', methods=["GET"])
@swag_from({
    'tags': ['News'],
    'parameters': [
        swag_param(PARAM.PATH, "news_id", VALUE.INTEGER)
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual news item',
            'schema': NewsModel.schema()
        }
    }
})
def get_news(news_id: str):
    res = refresh_news(time() // 60 // 60)
    ret = next(filter(lambda x: x["news_id"] == news_id, res), None)
    print(ret)
    if ret:
        # XXX create NewsModel then jsonify
        news = NewsModel(**ret)
        return NewsModel.schema()().jsonify(news), HTTPStatus.OK
    else:
        return "news_id not found", HTTPStatus.NOT_FOUND

@lru_cache(maxsize=2)
def refresh_news(t):
    '''rss fails'''

    req = urllib.request.Request(UQNEWS_RSS_URL)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    with urllib.request.urlopen(req) as rss:
        items = xmltodict.parse(rss.read())["rss"]["channel"]["item"]

    ret = []
    for i in items:
        created_at = datetime.strptime(i.get("pubDate"), "%a, %d %b %Y %H:%M:%S %z")
        image_url = None
        news_id = ''.join(c for c in i.get("guid") if c.isdigit())
        # XXX we're not using the NewsModel here since we need a list of such
        # objects
        #news = NewsModel(created_at=created_at, url=i.get("link"),
        #        content=i.get("description"), image_url=image_url,
        #        news_id=news_id, title=i.get("title"))
        news = {"created_at":created_at, "url":i.get("link"),
                "content":i.get("description"), "image_url":image_url,
                "news_id":news_id, "title":i.get("title")}
        ret.append(news)

    return ret

"""Get tha news"""

from .api_register import api_register

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
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
    return NewsModel.schema()().jsonify(res, many=True), HTTPStatus.OK

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
    if not ret:
        return "news_id not found", HTTPStatus.NOT_FOUND
    return NewsModel.schema()().jsonify(news), HTTPStatus.OK

def parse_news(item):
    created_at = datetime.strptime(item.get("pubDate"), "%a, %d %b %Y %H:%M:%S %z")
    image_url = None

    url = item.get("link")

    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    with urllib.request.urlopen(req) as res:
        soup = BeautifulSoup(res.read(), 'html.parser')
        img = soup.select('.uq-core-image img')
        if len(img) >= 1:
            image_url = img[0]['src']

    news_id = ''.join(c for c in item.get("guid") if c.isdigit())
    news = NewsModel(created_at=created_at, url=item.get("link"),
                     content=item.get("description"), image_url=image_url,
                     news_id=news_id, title=item.get("title"))
    return news

@lru_cache(maxsize=2)
def refresh_news(t):
    '''rss fails'''
    req = urllib.request.Request(UQNEWS_RSS_URL)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")

    with urllib.request.urlopen(req) as rss:
        items = xmltodict.parse(rss.read())["rss"]["channel"]["item"]

    with ThreadPoolExecutor() as executor:
        ret = list(executor.map(parse_news, items))

    return ret

refresh_news(time() // 60 // 60)
from .api_register import api_register

from apscheduler.schedulers.background import BackgroundScheduler
from flasgger import swag_from
from google.transit import gtfs_realtime_pb2
from http import HTTPStatus
from threading import Lock
from urllib import request

from api.model import VehicleModel
from utils.route_utils import swag_param, PARAM, VALUE

import flask


lakes = []
chancellors = []
lock = Lock()


def retrieve_feed():
    with lock:
        global lakes, chancellors
        feed = gtfs_realtime_pb2.FeedMessage()
        response = request.urlopen('https://gtfsrt.api.translink.com.au/api/realtime/SEQ')
        feed.ParseFromString(response.read())

        CHANCELLORS_ROUTE_IDS = ["402","411","412","414","427","428","432"]
        LAKES_ROUTE_IDS = ["139","169","192","209","28","29","66","P332"]

        LAKES_STOP_IDS = ["1882","1853","1877","1878","1880","1883"]

        CHANCELLORS_STOP_IDS = ["1801","1799","1798","1797","1802"]

        for entity in feed.entity:
          if entity.HasField('trip_update'):

            trip_update = entity.trip_update

            route_id = trip_update.trip.route_id.split('-')[0]
            
            lakes_stop = next(filter(lambda stu: stu.stop_id in LAKES_STOP_IDS, trip_update.stop_time_update), None)
            chancellors_stop = next(filter(lambda stu: stu.stop_id in CHANCELLORS_STOP_IDS, trip_update.stop_time_update), None)

            if lakes_stop:
              lakes.append(VehicleModel(code=route_id, 
                                        name=route_id, 
                                        eta=lakes_stop.departure.time))

            if chancellors_stop:
              chancellors.append(VehicleModel(code=route_id, 
                                        name=route_id, 
                                        eta=chancellors_stop.departure.time))

        lakes = sorted(lakes, key=lambda x: x.eta)
        chancellors = sorted(chancellors, key=lambda x: x.eta)


@api_register.route('/transport/lakes', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': VehicleModel.schema()
        }
    }
})
def transport_lakes():
    with lock:
        return VehicleModel.schema()().jsonify(lakes, many=True), HTTPStatus.OK


@api_register.route('/transport/lakes/<string:code>', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'parameters': [
        swag_param(PARAM.PATH, "code", VALUE.STRING)
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual transport item',
            'schema': VehicleModel.schema()
        }
    }
})
def transport_lakes_id(code: str):
    with lock:
        result = list(filter(lambda x: x[1] == code, lakes))
        return VehicleModel.schema()().jsonify(result, many=True), HTTPStatus.OK

@api_register.route('/transport/chancellors', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': VehicleModel.schema()
        }
    }
})
def transport_chancellors():
    with lock:
        return VehicleModel.schema()().jsonify(chancellors, many=True), HTTPStatus.OK


@api_register.route('/transport/chancellors/<string:code>', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'parameters': [
        swag_param(PARAM.PATH, "code", VALUE.STRING)
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual transport item',
            'schema': VehicleModel.schema()
        }
    }
})
def transport_chancellors_id(code: str):
    with lock:
        result = list(filter(lambda x: x[1] == code, chancellors))
        return VehicleModel.schema()().jsonify(result, many=True), HTTPStatus.OK

scheduler = BackgroundScheduler()
job = scheduler.add_job(retrieve_feed, 'interval', seconds=30)
scheduler.start()

retrieve_feed()

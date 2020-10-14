from http import HTTPStatus
import flask
from flasgger import swag_from
import api.model as models
from .api_register import api_register
from gtfslib.dao import Dao
from functools import lru_cache

from gtfslib.model import *
import datetime
import time
import threading

queue = []
queue_lock = threading.Lock()

@lru_cache(maxsize=1)
def start_server():
    threading.Thread(target=transport_server).start()
    time.sleep(10)

@api_register.route('/transport', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport():
    start_server()
    
    queue_lock.acquire()
    result = queue.copy()
    queue_lock.release()

    return flask.json.jsonify(result), 200

    result = models.VehicleModel()
    return models.VehicleModel.schema()().jsonify(result), 200


@api_register.route('/transport/<int:transportID>', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'parameters': [{
        'in': 'path',
        'name': 'transportID',
        'type': 'int',
        'required': 'true'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get an individual transport item',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport_id(transportID: int):
    result = []  # TODO FIX
    return models.VehicleModel.schema()().jsonify(result), 200

rightnow = lambda: time.time() // 1
thismin = lambda: rightnow() // 60
today = lambda: thismin() // 60 // 24

@lru_cache(maxsize=1)
def get_timetable():
    with open("uq_gtfs.sqlite", 'rb') as f, open('-uq_gtfs.sqlite', 'wb') as g:
        print('copying')
        block = f.read(2**15)
        while block:
            g.write(block)
            block = f.read(2**15)

    return Dao('-uq_gtfs.sqlite')

def buses_by_min(tt, minute):
    buses = []
    for s in tt.stops():
        for st in tt.stoptimes(fltr=((StopTime.stop == s) &
                (StopTime.departure_time >= minute * 60) &
                (StopTime.departure_time <= (minute + 1) * 60))):
            sttrip = next(t for t in tt.trips(fltr=(Trip.trip_id == st.trip_id)))
            stroute = next(r for r in tt.routes(fltr=(Route.route_id == sttrip.route_id)))
            buses.append({'eta': minute + today() * 60 * 60 * 24,
                          'name': stroute.route_long_name,
                          'code': stroute.route_short_name})

    return buses


def transport_server():
    tt = get_timetable()

    next_min = thismin() % (24 * 60)

    while True:
        queue_lock.acquire()
        to_del = []
        for i in range(len(queue)):
            if queue[i]['eta'] <= thismin() * 60:
                to_del.append(i)
            else:
                break

        for i,j in enumerate(to_del):
            del queue[j - i]

        while len(queue) < 50:
            queue.extend(buses_by_min(tt, next_min))
            next_min += 1
            next_min %= 60 * 24

        if queue[50:]:
            del queue[50:]

        queue_lock.release()
        time.sleep(60)

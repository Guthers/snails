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

lakes_queue = []
lakes_queue_lock = threading.Lock()
chancellors_queue = []
chancellors_queue_lock = threading.Lock()
init_lock = False

QUEUE_SIZE = 10

@lru_cache(maxsize=1)
def start_server():
    print('starting server')
    threading.Thread(target=transport_server).start()

@api_register.route('/transport-lakes', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport_lakes():
    global init_lock
    if not init_lock:
        start_server()

    print('to serve')
    while not init_lock: pass
    print('served')
    
    lakes_queue_lock.acquire()
    result = lakes_queue.copy()
    lakes_queue_lock.release()

    return flask.json.jsonify(result), 200

    result = models.VehicleModel()
    return models.VehicleModel.schema()().jsonify(result), 200


@api_register.route('/transport-lakes/<int:transportID>', methods=["GET"])
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
def transport_lakes_id(transportID: int):
    global init_lock
    if not init_lock:
        start_server()

    print('to serve')
    while not init_lock: pass
    print('served')

    lakes_queue_lock.acquire()
    result = lakes_queue[min(transportID, len(lakes_queue) - 1)]
    lakes_queue_lock.release()
    return models.VehicleModel.schema()().jsonify(result), 200

@api_register.route('/transport-chancellors', methods=["GET"])
@swag_from({
    'tags': ['Transport'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get a list of transport items',
            'schema': models.VehicleModel.schema()
        }
    }
})
def transport_chancellors():
    global init_lock
    if not init_lock:
        start_server()

    print('to serve')
    while not init_lock: pass
    print('served')
    
    chancellors_queue_lock.acquire()
    result = chancellors_queue.copy()
    chancellors_queue_lock.release()

    return flask.json.jsonify(result), 200

    result = models.VehicleModel()
    return models.VehicleModel.schema()().jsonify(result), 200


@api_register.route('/transport-chancellors/<int:transportID>', methods=["GET"])
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
def transport_chancellors_id(transportID: int):
    global init_lock
    if not init_lock:
        start_server()

    print('to serve')
    while not init_lock: pass
    print('served')

    chancellors_queue_lock.acquire()
    result = chancellors_queue[min(transportID, len(lakes_queue) - 1)]
    chancellors_queue_lock.release()
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

    print('done copying')
    print('Dao')
    result = Dao('-uq_gtfs.sqlite')
    print('done Dao')
    return result

def buses_by_min(stops, minute):
    tt = get_timetable()
    buses = []
    for s in stops:
        for st in tt.stoptimes(fltr=((StopTime.stop == s) &
                (StopTime.departure_time >= minute * 60) &
                (StopTime.departure_time < (minute + 1) * 60))):
            sttrip = next(t for t in tt.trips(fltr=(Trip.trip_id == st.trip_id)))
            stroute = next(r for r in tt.routes(fltr=(Route.route_id == sttrip.route_id)))
            buses.append({'eta': minute + today() * 60 * 60 * 24,
                          'name': stroute.route_long_name,
                          'code': stroute.route_short_name})

    return buses


def transport_server():
    global init_lock

    tt = get_timetable()

    next_min = thismin() % (24 * 60)
    s = next(tt.stops())
    lakes_stops = {s for s in tt.stops() if s.parent_station_id == 'place_UQLAKE'}
    chancellors_stops = {s for s in tt.stops() if s.parent_station_id == 'place_INTUQ'}
    time.sleep(10)

    while True:
        lakes_queue_lock.acquire()
        print('deleting old buses')
        to_del = []
        for i in range(len(lakes_queue)):
            if lakes_queue[i]['eta'] <= thismin() * 60:
                to_del.append(i)
            else:
                break

        for i,j in enumerate(to_del):
            del lakes_queue[j - i]

        while len(lakes_queue) < QUEUE_SIZE:
            lakes_queue.extend(buses_by_min(lakes_stops, next_min))
            next_min += 1
            next_min %= 60 * 24

        init_lock = True

        lakes_queue_lock.release()
        chancellors_queue_lock.acquire()
        print('deleting old buses')
        to_del = []
        for i in range(len(chancellors_queue)):
            if chancellors_queue[i]['eta'] <= thismin() * 60:
                to_del.append(i)
            else:
                break

        for i,j in enumerate(to_del):
            del chancellors_queue[j - i]

        while len(chancellors_queue) < QUEUE_SIZE:
            chancellors_queue.extend(buses_by_min(chancellors_stops, next_min))
            next_min += 1
            next_min %= 60 * 24

        init_lock = True

        chancellors_queue_lock.release()
        time.sleep(60)

from flask import Flask, Blueprint, request, abort, jsonify, make_response
from flask import request
import app.firstmodule.entities as entities
import time


module = Blueprint('', __name__)


@module.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@module.route('/flights', methods=['POST'])
def create_flight():
    new_flight = {
        'departure_time' : request.json['departure_time'],
        'arrival_time' : request.json['arrival_time'],
        'duration' : request.json['duration'],
        'arrive_location' : request.json['arrive_location'],
        'aircraft_type' : request.json['aircraft_type']
    }
    entities.flights.append(entities.Flight(new_flight))
    return jsonify({'flight': new_flight}), 201

@module.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = list(filter(lambda f: f.id == flight_id, entities.flights))
    if len(flight) == 0:
        abort(404)
    return jsonify({'flight': flight[0].convert_to_dict()})
    
@module.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@module.route('/flights', methods=['GET'])
def get_flights():
    all_flights = []
    for flight in entities.flights:
        all_flights.append(flight.convert_to_dict())
    return jsonify({'flights': all_flights})
    
@module.route('/flights/<int:flight_id>', methods=['PUT'])
def change_flight(flight_id):
    flight = list(filter(lambda f: f.id == flight_id, entities.flights))
    if len(flight) == 0:
        abort(404)
    flight = flight[0]
    flight.departure_time = request.json['departure_time']
    flight.arrival_time = request.json['arrival_time']
    flight.duration = request.json['duration']
    flight.arrive_location = request.json['arrive_location']
    flight.aircraft_type = request.json['aircraft_type']
    return jsonify({'flight': flight.convert_to_dict()})
    
@module.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    flight = list(filter(lambda f: f.id == flight_id, entities.flights))
    if len(flight) == 0:
        abort(404)
    flight = flight[0]
    entities.flights.remove(flight)
    return jsonify({'result': 'Successfully delete'})

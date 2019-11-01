from app.database import db
import app.firstmodule.models as models

def get_by_attr(table, attr, value):
    """
    Checks existance of attribute in table
    """
    return db.session.query(table).filter(attr==value).all()

def add_flight(request):
    '''
    new_flight = {
        'departure_time': request.json['departure_time'],
        'arrival_time': request.json['arrival_time'],
        'duration': request.json['duration'],
        'arrive_location': request.json['arrive_location'],
        'aircraft_type': request.json['aircraft_type']
    }'''
    plane = None
    airport = None
    try:
        plane = get_by_attr(models.Plane, models.Plane.name, request.json['aircraft_type'])[0]
        airport = get_by_attr(models.Airport, models.Airport.name, request.json['arrive_location'])[0]
    except IndexError:
        pass
    if not plane:
        plane = models.Plane(name=request.json['aircraft_type'])
        db.session.add(plane)
        db.session.commit()
    if not airport:
        airport = models.Airport(name=request.json['arrive_location'])
        db.session.add(airport)
        db.session.commit()
    new_flight = models.Flight(
        departure_time = request.json['departure_time'],
        arrival_time = request.json['arrival_time'],
        duration = request.json['duration'],
        arrive_airport = airport.airport_id,
        plane = plane.plane_id
        )
    db.session.add(new_flight)
    db.session.commit()
    
def get_all_flights():
    q = (db.session.query(models.Flight, models.Plane, models.Airport)
        .filter(models.Flight.plane == models.Plane.plane_id)
        .filter(models.Flight.arrive_airport == models.Airport.airport_id)
        .all())
    all_flights = []
    for el in q:
        dict_ = el[0].make_json_serializable()
        dict_.update(el[2].make_json_serializable())
        dict_.update(el[1].make_json_serializable())
        all_flights.append(dict_)
    return all_flights
    
def get_flight_by_id(flight_id):
    res = (db.session.query(models.Flight, models.Plane, models.Airport)
        .filter(models.Flight.plane == models.Plane.plane_id)
        .filter(models.Flight.arrive_airport == models.Airport.airport_id)
        .filter(models.Flight.flight_id == flight_id)
        .all())
    res = res[0]
    dict_ = res[0].make_json_serializable()
    dict_.update(res[2].make_json_serializable())
    dict_.update(res[1].make_json_serializable())
    return dict_
    
def modify_flight(request, flight_id, flight):
    plane = get_by_attr(models.Plane, models.Plane.name, request.json['aircraft_type'])[0]
    airport = get_by_attr(models.Airport, models.Airport.name, request.json['arrive_location'])[0]
    flight.departure_time = request.json['departure_time']
    flight.arrival_time = request.json['arrival_time']
    flight.duration = request.json['duration']
    flight.arrive_airport = airport.airport_id
    flight.plane = plane.plane_id
    db.session.commit()
    
def get_flight_object(flight_id):
    return db.session.query(models.Flight).filter(models.Flight.flight_id == flight_id)
    
def delete_flight(flight_id):
    db.session.query(models.Flight).filter(models.Flight.flight_id == flight_id).delete()
    db.session.commit()

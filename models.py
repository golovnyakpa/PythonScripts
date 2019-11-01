from app.database import db


class Plane(db.Model):
    __tablename__ = 'planes'
    plane_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    flights = db.relationship('Flight')
    
    def __repr__(self):
        return {
            'plane': self.name
            }
            
    def make_json_serializable(self):
        return {
            'plane': self.name
            }


class Airport(db.Model):
    __tablename__ = 'airports'
    airport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    flights = db.relationship('Flight')
    
    def __repr__(self):
        return {
            'arrive_location': self.name
            }
            
    def make_json_serializable(self):
        return {
            'arrive_location': self.name
            }


class Flight(db.Model):
    __tablename__ = 'flights'
    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    arrive_airport = db.Column(db.Integer, db.ForeignKey('airports.airport_id'),
                               nullable=False)
    plane = db.Column(db.Integer, db.ForeignKey('planes.plane_id'), 
                                                 nullable=False)
                                                 
    def make_json_serializable(self):
        return {
            'id': self.flight_id,
            'departure_time': str(self.departure_time),
            'arrival_time': str(self.arrival_time),
            'duration': str(self.duration)
            #'arrive_location': self.arrive_location,
            #'aircraft_type': self.aircraft_type
            }

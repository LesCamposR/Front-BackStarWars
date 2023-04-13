from flask_sqlalchemy import SQLAlchemy
from .db import db

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Float, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    favoriteVehicles = db.relationship('FavoriteVehicles', backref = 'vehicles', lazy= True )

    def serialize(self):
        return {
            "id": self.id,        
            "vehicle_class": self.diameter,
            "manufacturer": self.rotation_period,
            "cost_in_credits": self.orbital_period,
            "length": self.gravity,
            "crew": self.population,
            "passengers": self.climate,
            "max_atmosphering_speed": self.terrain,
            "cargo_capacity": self.surface_water,
            "name": self.name
            # do not serialize the password, its a security breach
        }
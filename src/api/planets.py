from flask_sqlalchemy import SQLAlchemy
from .db import db


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    favoritePlanets = db.relationship('FavoritePlanets', backref = 'planets', lazy= True )

    def serialize(self):
        return {
            "id": self.id,        
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "name": self.name
            # do not serialize the password, its a security breach
        }
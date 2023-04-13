from flask_sqlalchemy import SQLAlchemy
from .db import db

class FavoritePlanets (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable= False)
    
    def serialize(self):
        return {
            "id": self.id,
            "planets_id" : self.planets_id,
            "user_id" : self.user_id
        }
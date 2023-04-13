from flask_sqlalchemy import SQLAlchemy
from .db import db

class FavoriteVehicles (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable= False)
    
    def serialize(self):
        return {
            "id": self.id,
            "vehicles_id" : self.vehicles_id,
            "user_id" : self.user_id
        }
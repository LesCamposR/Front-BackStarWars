from flask_sqlalchemy import SQLAlchemy
from .db import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Float(50), unique=False, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    skin_Color = db.Column(db.String(120), unique=False, nullable=False)
    eye_Color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    favoritePeople = db.relationship('FavoritePeople', backref = 'people', lazy= True )

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_Color": self.skin_Color,
            "eye_Color": self.eye_Color,
            "birth_year": self.birth_year,
            "gender": self.gender
            # do not serialize the password, its a security breach
        }
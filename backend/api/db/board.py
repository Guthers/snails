from .db import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    longitude = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)

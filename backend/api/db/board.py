from .db import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key = True)
    longitude = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)

from .db import db

class UserDB(db.Model):
    studentID = db.Column(db.Integer, primary_key = True)
    studentname = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    createDate = db.Column(db.Date())
    eposts = db.relationship('Epost', backref='author', lazy=True)
    messagesSent = db.relationship('Umessage', backref='fromUser', lazy=True)
    messagesRecv = db.relationship('Umessage', backref='toUser', lazy=True)
    likes = db.relationship("Liked", backref="user", lazy=True)

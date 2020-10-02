from .db import db

class UserDB(db.Model):
    __tablename__="userdb"
    studentID = db.Column(db.String(255), primary_key = True)
    studentName = db.Column(db.String(255))
    bio = db.Column(db.String(255)) # pretty sure this doesn't work
    createDate = db.Column(db.Date())
    eposts = db.relationship('Epost', backref='author', lazy=True)
    messagesSent = db.relationship('Umessage', foreign_keys='Umessage.fromuserID', backref='fromUser', lazy=True)
    messagesRecv = db.relationship('Umessage', foreign_keys='Umessage.toUserID', backref='toUser', lazy=True)
    likes = db.relationship("Liked", backref="user", lazy=True)

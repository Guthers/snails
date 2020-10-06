from .db import db

class UserDB(db.Model):
    __tablename__="userdb"
    student_id = db.Column(db.String(255), primary_key = True)
    student_name = db.Column(db.String(255))
    bio = db.Column(db.String(255)) # pretty sure this doesn't work
    create_date = db.Column(db.Date())
    eposts = db.relationship('Epost', backref='author', lazy=True)
    messages_sent = db.relationship('Umessage',
            foreign_keys='Umessage.from_user_id', backref='from_user', lazy=True)
    messagesRecv = db.relationship('Umessage',
            foreign_keys='Umessage.to_user_id', backref='to_user', lazy=True)
    likes = db.relationship("Liked", backref="user", lazy=True)

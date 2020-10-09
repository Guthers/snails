from .db import db
import datetime

class Umessage(db.Model):
    message_id = db.Column(db.Integer, primary_key = True)
    message_content = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    from_user_id = db.Column(db.String(255), db.ForeignKey('userdb.student_id'))
    to_user_id = db.Column(db.String(255), db.ForeignKey('userdb.student_id'))

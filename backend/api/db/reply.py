from .db import db

class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('epost.post_id'))
    user_id = db.Column(db.String(255), db.ForeignKey('userdb.student_id'))
    create_date = db.Column(db.Date())
    replied_to_name = db.Column(db.String(255))

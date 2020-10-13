from .db import db

class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key = True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.Date())
    replied_to_name = db.Column(db.String(255))

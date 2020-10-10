from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
db.drop_all()
db.create_all()

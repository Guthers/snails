from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
db.create_all()

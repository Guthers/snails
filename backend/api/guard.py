from app import app
from flask_praetorian import Praetorian
from api.db import User

guard = Praetorian()
# Initialise the flask-praetorian instance for the app
guard.init_app(app, User)

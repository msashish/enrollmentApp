from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine


app = Flask(__name__)

# load configuration to app
app.config.from_object(Config)

# Get Mongodb instance
db = MongoEngine()

# Initialise unique Mongodb instance for the app so that multiple apps do not use same instance
db.init_app(app)

from application import routes

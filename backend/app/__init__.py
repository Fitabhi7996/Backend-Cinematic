from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/cinematic_event_management"
mongo = PyMongo(app)

from app import routes

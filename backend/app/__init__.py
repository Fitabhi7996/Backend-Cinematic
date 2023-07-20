from flask import Flask
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://ghodmareabhishek:5de4tAfbQ8drhQoS@cluster0.qa52dcw.mongodb.net/cinematic_event_management?retryWrites=true&w=majority"
mongo = PyMongo(app)

from app import routes

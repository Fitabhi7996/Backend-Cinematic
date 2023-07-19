from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://ghodmareabhishek:abhishek@cluster0.p2izv8b.mongodb.net/cinematic_event_management?retryWrites=true&w=majority"
mongo = PyMongo(app)

from app import routes

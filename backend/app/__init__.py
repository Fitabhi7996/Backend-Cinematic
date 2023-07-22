from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://ghodmareabhishek:5de4tAfbQ8drhQoS@cluster0.qa52dcw.mongodb.net/cinematic_event_management?retryWrites=true&w=majority"
mongo = PyMongo(app)



from app import routes

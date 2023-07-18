from flask import jsonify, request
from app import app, mongo

# User endpoints
@app.route("/api/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    return jsonify(users)

@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify(user)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = {
        "username": data["username"],
        "status": data["status"],
        "gender": data["gender"],
        "membership_type": data["membership_type"],
        "bio": data["bio"],
        "date_of_birth": data["date_of_birth"]
    }
    result = mongo.db.users.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return jsonify(user), 201

@app.route("/api/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    updated_user = {
        "username": data["username"],
        "status": data["status"],
        "gender": data["gender"],
        "membership_type": data["membership_type"],
        "bio": data["bio"],
        "date_of_birth": data["date_of_birth"]
    }
    mongo.db.users.update_one({"_id": user_id}, {"$set": updated_user})
    return jsonify(updated_user)

@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": user_id})
    return jsonify({"message": "User deleted"})

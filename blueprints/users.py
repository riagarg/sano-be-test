from flask import Blueprint, jsonify
from models import User
from schemas import UserSchema

users_api = Blueprint("users_api", __name__)


@users_api.route("/users")
def get_all_users():
    all_users = User.select()
    data = UserSchema().dump(all_users, many=True)
    return jsonify({"data": data, "count": len(data)})

from flask import Blueprint, jsonify
from core.schemas import UserSchema

users_api = Blueprint("users_api", __name__)


@users_api.route("/users", methods=["GET"])
def get_all_users():
    # ...
    # return jsonify({"data": data, "count": len(data)})
    raise NotImplementedError
from models import db
from models.user import User
from flask import Blueprint, request


user_api_routes = Blueprint(name="user", import_name=__name__, url_prefix="/user")


@user_api_routes.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return {"data": [
        {
            "firstname": u.firstname,
            "lastname": u.lastname,
            "email": u.email,
        } for u in users]
    }


@user_api_routes.route("/<id>", methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return {
            "status": "Error",
            "description": "User not found"
        }, 404
    return {"data": {
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
        }
    }


@user_api_routes.route("/firstname/<firstname>", methods=["GET"])
def get_user_by_firstname(firstname):
    users = User.query.filter(User.firstname == firstname)
    return {"data": [
        {
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
        } for user in users]
    }


@user_api_routes.route("/", methods=["POST"])
def create_user():
    user = request.json
    print(user)
    user = User(
        firstname=user["prenom"],
        lastname=user["nom"],
        email=user["email"],
        password=user["password"]
    )
    db.session.add(user)
    db.session.commit()
    return {
        "status": "Success"
    }


from models import db
from models.user import User
from flask import Blueprint, request


# user_list = [
#     User(firstname="Mathilde", lastname="Dubois", password="okok", email="md@md.com")
# ]
user_api_routes = Blueprint(name="user", import_name=__name__, url_prefix="/user")

@user_api_routes.route("/", methods=["GET"])
def get_users():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User(
            firstname=prenom,
            lastname=nom,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return {"data": [
        {
            "firstname": u.firstname,
            "lastname": u.lastname,
            "email": u.email,
        } for u in users]
    }

@user_api_routes.route("/", methods=["POST"])
def create_user():
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    email = request.form.get("email")
    password = request.form.get("password")
    user = User(
        firstname=prenom,
        lastname=nom,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return {
        "status": "Success"
    }


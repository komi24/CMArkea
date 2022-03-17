from flask import Blueprint, render_template, request
from models.user import User
from models import db
from auth import flask_bcrypt
from flask_login import login_user


auth_routes = Blueprint(name="auth", import_name=__name__, url_prefix="/auth")


@auth_routes.route("/login")
def login():
    return render_template("login.html")


@auth_routes.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        email = request.form.get("email")
        password = request.form.get("password")
        password_hash = flask_bcrypt.generate_password_hash(password)
        user = User(
            firstname=prenom,
            lastname=nom,
            email=email,
            password=password_hash,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)

    return render_template("signup.html")


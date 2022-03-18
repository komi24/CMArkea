from flask import Blueprint, render_template, request, redirect
from models.user import User
from models import db
from auth import flask_bcrypt, login_manager
from flask_login import login_user


auth_routes = Blueprint(name="auth", import_name=__name__, url_prefix="/auth")


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user_found = User.query.filter(User.email == email).first()
        if user_found and flask_bcrypt.check_password_hash(user_found.password, password):
            login_user(user_found)
            return redirect("/")
        else:
            return render_template("login.html", error_message="Login failed")

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
        return redirect("/")

    return render_template("signup.html")


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect("/auth/login")
import flask_login
from flask import Flask, render_template, request
from models import db
from models.user import User
from api.routes import api_routes
from auth.routes import auth_routes
from auth import login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = "mon_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arkea.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(api_routes)
app.register_blueprint(auth_routes)

with app.app_context():
    db.init_app(app)
    db.create_all()
    login_manager.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    contact_list = [
        {"name": "Service Commercial", "horaires": "Ouvert du Lundi au Vendredi de 9h à 17h"},
        {"name": "Service RH", "horaires": "Ouvert du Lundi au Vendredi de 10h à 16h"},
    ]
    return render_template("contact.html", contact_list=contact_list)


@app.route("/users")
@flask_login.login_required
def user_list():
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/form", methods=["POST"])
def form_handler():
    print(request.form.get("nom"))
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

    return render_template("index.html", lastname=nom, firstname=prenom)


app.run(port=8080, debug=True)

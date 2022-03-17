from flask import Flask, render_template, request
from models import db
from models.user import User
from api.routes import api_routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arkea.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(api_routes)

with app.app_context():
    db.init_app(app)
    db.create_all()


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

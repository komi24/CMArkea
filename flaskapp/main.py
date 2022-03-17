from flask import Flask, render_template, request

app = Flask(__name__)
# print(__name__)


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
    return render_template("index.html", lastname=nom, firstname=prenom)

app.run(port=8080, debug=True)

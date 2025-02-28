from flask import Flask, render_template, url_for, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://Arturo:<db_password>@crud.qnjuw.mongodb.net/?retryWrites=true&w=majority&appName=Crud"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["flaskgames"]
datos = db.datos


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/añadir", methods=["GET", "POST"])
def añadir():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        color = request.form.get("color")
        animal = request.form.get("animal")

        datos.insert_one({"nombre": nombre, "apellido": apellido, "color": color, "animal":animal})
        print ("Añadido con exito")

    return render_template("añadir.html")


if __name__ == ("__main__"):
    app.run(debug=True)
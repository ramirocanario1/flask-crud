from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User
from utils.db import db

users = Blueprint("users", __name__)


@users.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)


@users.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    user = User(username, password, email)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("users.home"))


@users.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    user = User.query.get(id)

    # Si el método es POST, es porque se cargó el formulario con datos y se enviaron para la actualización
    if request.method == "POST":
        user.username = request.form["username"]
        user.password = request.form["password"]
        user.email = request.form["email"]

        db.session.commit()
        return redirect(url_for("users.home"))
    else:
        # Si el método es GET, es porque se ingresó a la URL para editar,
        # por lo que tengo que retornar el template con los datos para que se carguen
        return render_template("update.html", user=user)


@users.route("/delete/<id>")
def delete(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("users.home"))

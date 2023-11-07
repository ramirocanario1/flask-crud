from flask import Flask
from routes.users import users
from utils.db import db

app = Flask(__name__)

db_user = "postgres"
db_password = "ramiro"
db_host = "localhost"
db_database_name = "flask_db"

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{db_user}:{db_password}@{db_host}/{db_database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(users)

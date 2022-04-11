import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

viewgerapp = Flask(__name__)
viewgerapp.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(viewgerapp)
migrate = Migrate(viewgerapp, db)


@viewgerapp.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    viewgerapp.run()

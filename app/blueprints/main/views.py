from flask import Blueprint, render_template

blueprint = Blueprint("main", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

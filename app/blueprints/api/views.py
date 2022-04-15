from flask import Blueprint, render_template

blueprint = Blueprint("api", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("api.html")

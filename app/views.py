from flask import Blueprint, current_app, render_template

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    current_app.run()

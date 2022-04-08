from flask import Flask, render_template

"""
Creates basic one-page Flask app
"""
viewgerapp = Flask(__name__)


@viewgerapp.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    viewgerapp.run(debug=True)  # add debug mode that allows to apply changes instantly

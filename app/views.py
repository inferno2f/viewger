from flask import current_app, render_template


@current_app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    current_app.run()

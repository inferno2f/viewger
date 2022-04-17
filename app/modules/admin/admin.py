from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from app.modules.user.models import User

"""
TO-DO: auth with Flask-Security
Ref.: https://github.com/flask-admin/flask-admin/blob/master/examples/auth
"""


def init_app(app, db, name="Admin", url_prefix="/admin", **kwargs):
    vkwargs = {"name": name, "endpoint": "admin", "url": url_prefix}

    akwargs = {
        "template_mode": "bootstrap3",
        "static_url_path": f"/templates{url_prefix}",
        "index_view": AdminIndexView(**vkwargs),
    }

    admin = Admin(app, **akwargs)
    admin.add_view(ModelView(User, db.session))

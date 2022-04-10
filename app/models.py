from views import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128))
    grade = db.Column(db.String(24))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, username, email, result_all, result_no_stop_words):
        self.username = username
        self.email = email
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return f'{self.username} - id: {self.id}'

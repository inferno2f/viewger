from sqlalchemy.sql import expression

from app.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True)
    grade = db.Column(db.String(24))
    is_admin = db.Column(db.Boolean, server_default=expression.false(), nullable=False)

    def __repr__(self):
        return f"{self.username} - id: {self.id}"
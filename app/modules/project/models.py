from sqlalchemy import ForeignKey

from app.db import db


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
    description = db.Column(db.VARCHAR)
    started_at = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class Member(db.Model):
    __tablename__ = "member"

    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey('skill.id'))
    role = db.Column(db.Enum)

    def __repr__(self):
        return f"user_id {self.user_id} - project_id {self.skill_id}"

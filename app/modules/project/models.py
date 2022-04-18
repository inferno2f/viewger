from sqlalchemy import ForeignKey

from app.db import db


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.VARCHAR, nullable=False)
    started_at = db.Column(db.TIMESTAMP, nullable=False)

    projects = db.relationship('Project', backref=db.backref('pull_request', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


# class Member(db.Model):
#     __tablename__ = "member"
#
#     user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
#     project_id = db.Column(db.Integer, ForeignKey('skill.id'))
#     role = db.Column(db.Enum)
#
#     def __repr__(self):
#         return f"user_id {self.user_id} - project_id {self.skill_id}"

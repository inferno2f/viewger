from sqlalchemy.dialects.postgresql import ENUM as pgEnum

from app.db import db


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.VARCHAR, nullable=False)
    started_at = db.Column(db.TIMESTAMP, nullable=False)

    pull_requests = db.relationship('PullRequest', backref=db.backref('project', lazy=True))
    members = db.relationship('Member', backref=db.backref('project', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class Member(db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    role = db.Column(pgEnum(name='role'))

    def __repr__(self):
        return f"user_id {self.user_id} - project_id {self.skill_id}"

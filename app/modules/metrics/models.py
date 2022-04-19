from sqlalchemy import ForeignKey

from app.db import db


class Skill(db.Model):
    __tablename__ = "skill"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.VARCHAR, unique=True)
    name = db.Column(db.VARCHAR, unique=True)

    pr_skills = db.relationship('Skill', backref=db.backref('pr_skill', lazy=True))
    user_skills = db.relationship('Skill', backref=db.backref('user_skill', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class PRSkill(db.Model):
    __tablename__ = "pr_skill"

    pr_id = db.Column(db.Integer, ForeignKey('pull_request.id'), primary_key=True)
    skill_id = db.Column(db.Integer, ForeignKey('skill.id'))

    def __repr__(self):
        return f"pr_id {self.pr_id} - skill_id {self.skill_id}"


class UserSkill(db.Model):
    __tablename__ = "user_skill"

    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    skill_id = db.Column(db.Integer, ForeignKey('skill.id'))

    def __repr__(self):
        return f"user_id {self.user_id} - skill_id {self.skill_id}"

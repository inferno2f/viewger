from app.db import db


class Skill(db.Model):
    __tablename__ = "skill"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(16), unique=True, nullable=False)

    pr_skills = db.relationship('PRSkill', backref=db.backref('skill', lazy=True))
    user_skills = db.relationship('UserSkill', backref=db.backref('skill', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class PRSkill(db.Model):
    __tablename__ = "pr_skill"

    pr_id = db.Column(db.Integer, db.ForeignKey('pull_request.id'), primary_key=True, nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f"pr_id {self.pr_id} - skill_id {self.skill_id}"


class UserSkill(db.Model):
    __tablename__ = "user_skill"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f"users_id {self.users_id} - skill_id {self.skill_id}"

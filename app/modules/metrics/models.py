from app.db import db


class Skill(db.Model):
    __tablename__ = "skill"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.VARCHAR, unique=True, nullable=False)
    name = db.Column(db.VARCHAR, unique=True, nullable=False)

    pr_skills = db.relationship('PRSkill', backref=db.backref('skill', lazy=True))
    user_skills = db.relationship('UserSkill', backref=db.backref('skill', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class PRSkill(db.Model):
    __tablename__ = "pr_skill"

    id = db.Column(db.Integer, primary_key=True)
    pr_id = db.Column(db.Integer, db.ForeignKey('pull_request.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    def __repr__(self):
        return f"pr_id {self.pr_id} - skill_id {self.skill_id}"


class UserSkill(db.Model):
    __tablename__ = "user_skill"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    def __repr__(self):
        return f"users_id {self.users_id} - skill_id {self.skill_id}"

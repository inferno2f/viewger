from app.db import db


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    started_at = db.Column(db.DateTime, nullable=False)

    pull_requests = db.relationship('PullRequest', backref=db.backref('project', lazy=True))
    members = db.relationship('Member', backref=db.backref('project', lazy=True))

    def __repr__(self):
        return f"{self.name} - id: {self.id}"


class Member(db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    role = db.Column(db.Enum(name='roles'))

    def __repr__(self):
        return f"user_id {self.user_id} - project_id {self.skill_id}"

from sqlalchemy import ForeignKey

from app.db import db


class PullRequest(db.Model):
    __tablename__ = "pull_request"

    id = db.Column(db.Integer, primary_key=True)
    jira_task_id = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    author_id = db.Column(db.Integer, ForeignKey('user.id'))
    opened_at = db.Column(db.TIMESTAMP)
    closed_at = db.Column(db.TIMESTAMP)
    project_id = db.Column(db.Integer, ForeignKey('project.id'))

    def __repr__(self):
        return f"{self.jira_task_id} - id: {self.id}"


class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    pr_id = db.Column(db.Integer, ForeignKey('pull_request.id'))
    reviewer_id = db.Column(db.Integer, ForeignKey('user.id'))
    start_at = db.Column(db.TIMESTAMP)
    upd_at = db.Column(db.TIMESTAMP)
    status = db.Column(db.Enum)

    def __repr__(self):
        return f"{self.pr_id} - id: {self.id}"

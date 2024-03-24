import datetime
from app.main import db


class User(db.Model):
    """user model for storing user data"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, username: str, email: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.email = email
        self.password = password

    def set_updated_at(self, time: datetime):
        self.updated_at = time

    def set_created_at(self, time: datetime):
        self.created_at = time

    def set_deleted_at(self, time: datetime):
        self.deleted_at = time

    def __repr__(self):
        return "<User '{}'>".format(self.username)

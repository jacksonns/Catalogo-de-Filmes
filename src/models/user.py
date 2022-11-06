from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    wantToWatchList = db.Column(db.PickleType, nullable=True)
    watchedList = db.Column(db.PickleType, nullable=True)

    def verify_password(self, password):
        return self.password == password

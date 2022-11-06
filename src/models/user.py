from sqlalchemy import PickleType
from sqlalchemy.ext.mutable import MutableList

from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    wantToWatchList = db.Column(MutableList.as_mutable(PickleType))
    watchedList = db.Column(MutableList.as_mutable(PickleType))

    def verify_password(self, password):
        return self.password == password


def is_valid(user, password):
    if user is None:
        return False
    if password != user.password:
        return False
    return True
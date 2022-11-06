from app import db
from src.models.user import User

class MovieList(db.Model):
    __tablename__ = 'movie_list'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    overview = db.Column(db.String(255))
    poster = db.Column(db.String(255))
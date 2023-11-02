# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    director = db.Column(db.String(255), nullable = False)
    rating = db.Column(db.Integer, nullable = True)

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self) -> str:
        return f'Movie (title = {self.title}, director = {self.director}, rating = {self.rating})'
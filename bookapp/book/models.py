# Entity

from book import db

from sqlalchemy import text


class Book(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # text
    author = db.Column(db.String(50), nullable=False)  # text
    price = db.Column(db.Integer, nullable=False)  # text
    description = db.Column(db.Text())  # textarea
    created = db.Column(db.DateTime(), nullable=False)


# 사용자
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)  # text
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

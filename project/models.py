from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
#    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#    child = db.relationship("Pair", backfer='User')


# class Pair(db.Model):
#     __tablename__ = "Pair"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     label = db.Column(db.String(40), unique=True)
#     volume = db.Column(db.Integer)
#     spread = db.Column(db.Integer)
#     deep = db.Column(db.Integer)

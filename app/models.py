from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__= "pitches"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    author = db.Column(db.String(), nullable=False)
    description= db.Column(db.String(), nullable=False)
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'Pitch {self.author}'

class Category(db.Model):
    __tablename__="categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(), nullable=False)
    pitches = db.relationship('Pitch',backref = 'category',lazy="dynamic")

def __repr__(self):
        return f'Category {self.name}'
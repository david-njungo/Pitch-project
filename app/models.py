from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
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
from datetime import datetime

#from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationship: One user can have many recipes
    recipes = db.relationship('post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key: link to user who posted it
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # One recipe can have many ingredients
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
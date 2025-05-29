from datetime import datetime
#from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# will add user later and create the relationship

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     # Relationship: One user can have many recipes
#     recipes = db.relationship('post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'post'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Post {self.id} by {self.author}>"

    # foreign key: link to user who posted it
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # one recipe can have many ingredients
    # ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
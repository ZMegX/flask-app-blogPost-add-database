from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# will add user later and create the relationship

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    # relationship: One user can have many post
    post = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # foreign key to User table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    message = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Post {self.id} by {self.user_id}>"

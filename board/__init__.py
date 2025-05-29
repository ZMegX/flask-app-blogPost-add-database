import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_by_name
from board import pages, posts, database
from dotenv import load_dotenv


load_dotenv()

env = os.getenv('FLASK_ENV', 'development')
app = Flask(__name__)
app.config.from_object(config_by_name[env])

# Initialize DB
from models import db  # Make sure db is defined in models.py
db.init_app(app)

migrate = Migrate(app, db)

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app

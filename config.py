import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///test3.db')
    DEBUG = True

# when deploying on render you need to pass the internal URL of the database Server hosted on render.com
# set up your environnement in the web app that you're deploying, all URL must match for prod

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://foodissimotest_user:61JGFa44MX6pioBgxbEiTUH7rr4dEOfT@dpg-d108af3e5dus739e0h8g-a/foodissimotest')    
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

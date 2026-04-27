import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///proyecto_academy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

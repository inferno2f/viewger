import os
from pathlib import Path

from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "dev"  # should be changed for production version
    DB_USER = os.environ.get("DB_USER", "user")
    DB_PASS = os.environ.get("DB_PASS", "password")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", 5432)
    DB_NAME = os.environ.get("DB_NAME", "viewgerdb")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITLAB_URL = os.environ.get('GITLAB_URL')
    GITLAB_TOKEN = os.environ.get('GITLAB_TOKEN')
    REVIEWER_ID = 70755 # Ivan Golikov
    PROJECT_ID = 131110 # Viewger project

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

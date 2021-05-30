from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DEBUG = environ.get("DEBUG")
SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")




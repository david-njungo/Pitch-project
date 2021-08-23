import secrets
import os

class Base:
    FLASK_APP = os.environ.get('FLASK_APP')
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex()

class Development(Base):
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DATABASE = os.environ.get("pitchproject")
    POSTGRES_USER = os.environ.get("moringa")
    POSTGRES_PASSWORD = os.environ.get("1234")
    SQLALCHEMY_DATABASE_URI = os.environ.get("db+driver://moringa:1234@localhost/pitchproject")

class Staging(Base):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = ""

class Production(Base):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI= ""
   
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
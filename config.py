import secrets
import os

class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex()

class DevConfig(Config):
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DATABASE = os.environ.get("pitchproject")
    POSTGRES_USER = os.environ.get("moringa")
    POSTGRES_PASSWORD = os.environ.get("1234")
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:1234@localhost/pitchproject'

class ProdConfig(Config):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = ""
   
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
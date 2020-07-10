import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_ARTICLES_API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:my_postgres_password@localhost/pitch2'
    UPLOADED_PHOTOS_DEST = 'app/static'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:my_postgres_password@127.0.0.1:5432/moringa?sslmode=require
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://postgres:Access@localhost/pitch2'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://postgres:my_postgres_password@localhost/pitch2'

    DEBUG = True
    ENV = 'development'


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
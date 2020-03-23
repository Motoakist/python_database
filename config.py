import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

class DevelopmentConfig:
    # This turns on debug mode in Flask
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/PORTFOLIO?charset=utf8'.format(**{
                                'user': os.environ.get('MYSQL_USER', 'root'),
                                'password': os.environ.get('MYSQL_PASSWORD', 'root'),
                                'host': os.environ.get('DB_HOST', 'localhost:8889'),
                             })
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
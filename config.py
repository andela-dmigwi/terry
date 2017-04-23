""" Created by Migwi Ndung'u  @April 2017"""
import os
from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

verify_token = os.environ['VERIFY_TOKEN']
params = {"access_token": os.environ['PAGE_ACCESS_TOKEN']}
fb_url = os.environ['FB_URL']
main_url = 'http://terry.herokuapp.com'
JWT_SECRET = os.environ['SECRET']
JWT_ALGORITHM = 'HS256'
# ENV = os.environ('ENV')
DATABASE_URL = os.environ['MONGODB_URI']
json_headers = {"Content-Type": "application/json"}
# class Config(object):
#     TESTING = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     SECRET_KEY = 'confidential_top_secret!'
#     TRAP_HTTP_EXCEPTIONS = False
#     PRESERVE_CONTEXT_ON_EXCEPTION = False


# class Test(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:terry:'
#     DEBUG = True


# class Development(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/terry.db'.format(BASEDIR)
#     DEBUG = True


# class Production(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/terry.db'.format(BASEDIR)
#     DEBUG = False

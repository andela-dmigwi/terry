""" Created by Migwi Ndung'u  @April 2017"""
import os
from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

verify_token = os.environ['VERIFY_TOKEN']
page_access_token = os.environ['PAGE_ACCESS_TOKEN']
fb_url = os.environ['FB_URL']
main_url = 'http://terry.herokuapp.com'
JWT_SECRET = os.environ['SECRET']
JWT_ALGORITHM = 'HS256'
ENV = os.environ('ENV')
DATABASE_URL = os.environ['DATABASE_URL']

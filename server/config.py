import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "please_dont_crack_this"

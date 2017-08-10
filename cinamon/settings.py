import os

__author__ = 'tkolter'


DATABASE_NAME = os.environ.get('DATABASE_NAME', 'synonyms')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 27017)

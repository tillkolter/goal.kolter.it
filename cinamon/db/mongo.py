from pymongo import MongoClient

from cinamon import settings

__author__ = 'tkolter'


client = MongoClient(settings.DATABASE_HOST, settings.DATABASE_PORT)
db = client[settings.DATABASE_NAME]

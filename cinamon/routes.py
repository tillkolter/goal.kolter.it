from flask import (
    Flask,
)
from flask_restful import Api

from cinamon.resources import SynonymList, Synonym

__author__ = 'tkolter'


app = Flask(__name__)
api = Api(app)

api.add_resource(SynonymList, '/cinamon/synonyms')
api.add_resource(Synonym, '/cinamon/synonyms/<synonym_id>', endpoint='synonym')

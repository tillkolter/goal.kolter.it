import json

from bson import ObjectId
from flask import request, Response, url_for, abort
from flask_restful import Resource

from cinamon.db.mongo import db
from cinamon.schema import SynonymSchema

__author__ = 'tkolter'


class SynonymDao:

    def __init__(self, word, meaning_id):
        self._words = {word}
        self._meaning = word
        self.meaning_id = meaning_id

    def add_word(self, word):
        self._words.add(word)

    def is_synonym(self, other):
        if isinstance(other, SynonymDao):
            return self.meaning_id == other.meaning_id
        else:
            return other in self._words

    def merge(self, other):
        self._words |= other.words
        if other.meaning in self._words:
            if self.meaning not in other.words:
                self._meaning = other.meaning

    @property
    def json(self):
        return json.dumps({
            "id": self.meaning_id,
            "meaning": self.meaning,
            "words": list(self.words)
        })

    @property
    def words(self):
        return self._words

    @property
    def meaning(self):
        return self._meaning


class Synonym(Resource):

    def get(self, synonym_id):
        synonym = db.synonyms.find_one({"_id": ObjectId(synonym_id)})
        if synonym is None:
            abort(404)
        return json.loads(SynonymDao(synonym['meaning'], synonym_id).json)


class SynonymList(Resource):

    def post(self):

        synonym = SynonymSchema().load(json.loads(request.data.decode('utf-8')))
        if synonym.errors:
            return synonym.errors, 400
        inserted_id = db.synonyms.insert_one(synonym.data).inserted_id
        synonym_dao = SynonymDao(synonym.data['meaning'], str(inserted_id))
        resp = Response(
            mimetype='application/json'
        )
        resp.set_data(synonym_dao.json)
        resp.headers['Location'] = url_for('synonym', synonym_id=inserted_id)
        return resp



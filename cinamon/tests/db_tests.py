import json
from unittest import TestCase

from cinamon.db.mongo import db
from cinamon.resources import SynonymDao

__author__ = 'tkolter'


class DatabaseTest(TestCase):

    def test_synonym(self):
        bank = SynonymDao('Bank', 1)
        collection = db.test_collection
        synonyms = collection.synonyms
        synonyms.insert_one(json.loads(bank.json))
        found_bank = synonyms.find_one({
            'meaning': 'Bank'
        })
        self.assertEquals(1, found_bank['id'])
        self.assertIn('Bank', found_bank['words'])
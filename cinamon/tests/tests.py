import json
from unittest import TestCase

from cinamon.resources import SynonymDao

__author__ = 'tkolter'


class SynonymTest(TestCase):

    def test_meaning(self):
        s = SynonymDao("Bank", 1)
        self.assertEquals(s.meaning, "Bank")

    def test_meaning_is_word(self):
        s = SynonymDao("Bank", 1)
        self.assertTrue(s.meaning in s.words)

    def test_add_word(self):
        s = SynonymDao("Bank", 1)
        s.add_word("bench")
        self.assertTrue("bench" in s.words)

    def test_merge(self):
        bank = SynonymDao("Bank", 1)
        bench = SynonymDao("bench", 2)
        bank.merge(bench)
        self.assertTrue("bench" in bank.words)

    def test_merge_can_change_meaning(self):
        bank = SynonymDao("Bank", 1)
        bank.add_word("bench")
        bench = SynonymDao("bench", 2)
        bank.merge(bench)
        self.assertTrue("bench" in bank.meaning)

    def test_json(self):
        bank = SynonymDao("Bank", 1)
        bank.add_word("Schalter")
        bank_dict = json.loads(bank.json)
        self.assertTrue('Schalter' in bank_dict['words'])

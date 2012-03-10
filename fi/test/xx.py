'''Unittests for one_character_misspelling_suggestions.'''
import unittest
from ocms import suggestions
from ocms.words import Words

class Word_List(unittest.TestCase):
    def runTest(self):
        assert len(Words) > 200500

class Scale(unittest.TestCase):
    def runTest(self):
        x = suggestions('cale')
        assert 'scale' in x

class Causes(unittest.TestCase):
    def runTest(self):
        x = suggestions('causes')
        assert x == set(['cause', 'cruses', 'causes', 'causer',
            'causeys', 'causen', 'pauses', 'caused', 'cauves',
            'hauses', 'camuses', 'carses', 'causey', 'cayuses', 
            'chuses', 'caules', 'clauses', 'cases', 'causers'])

class BadInput(unittest.TestCase):
    def runTest(self):
        self.assertRaises(Exception, suggestions, None)

class UpperCase(unittest.TestCase):
    def runTest(self):
        self.assertRaises(Exception, suggestions, 'AB')

class Punct(unittest.TestCase):
    def runTest(self):
        self.assertRaises(Exception, suggestions, ')aa')
            
class Digits(unittest.TestCase):
    def runTest(self):
        self.assertRaises(Exception, suggestions, 'count0')

class Eric(unittest.TestCase):
    def runTest(self):
        x = suggestions('eric')
        assert len(x) == 11

class Xxxxxxxxxxxxxxx(unittest.TestCase):
    def runTest(self):
        x = suggestions('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        assert not x

            

'''Unittests for one_character_misspelling_suggestions.'''
import unittest
from network import count

class CountNetwork(unittest.TestCase):
    def runTest(self):
        n = count('causes')
        print n
        assert n > 74000

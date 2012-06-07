'''Unittests for one_character_misspelling_suggestions.'''
import unittest
from ocms import suggestions
from ocms.words import Words
import logging
import time
from anagrams import word_data

class Anagrams_Test(unittest.TestCase):
    def runTest(self):
        assert(word_data['ackkns'] == ['knacks'])

class Anagram_Dump(unittest.TestCase):
    def runTest(self):
        from collections import defaultdict
        _start = time.clock()
        word_data = defaultdict(list)
        for i in Words:
            word_data[''.join(sorted(i))].append(i)
        logging.info('word_data %.2f' % (time.clock() - _start))
        dict_file = open('/Volumes/FAT/dev/fi/anagrams.py', 'w')
        dict_file.write("word_data = {\n")
        for signature in word_data:
            dict_file.write("'%s': ['%s'],\n" % (signature, "', '".join(word_data[signature])))
        dict_file.write("}\n")
        n = dict_file.tell()
        print n
        dict_file.close()
        assert n > 200500

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

            

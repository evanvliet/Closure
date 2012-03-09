'''Report size of social network.

Two words are friends if they have a Levenshtein distance
(http://en.wikipedia.org/wiki/Levenshtein_distance) of 1. 
That is, you can add, remove, or substitute exactly one 
letter in word X to create word Y. A word's social network 
consists of all of its friends, plus all of their friends, 
and all of their friends' friends, and so on. Tell how big
the social network for the word "causes" is, using words from
(https://github.com/causes/puzzles/raw/master/word_friends/word.list).
'''
import time
import urllib
#_Words = set([word.strip() for word in urllib.urlopen(
#    'https://github.com/causes/puzzles/raw/master/word_friends/word.list')])
_Words = set([word.strip() for word in open('word.list')])
_Letters = 'abcdefghijklmnopqrstuvwxyz'

def _friends(word):
    '''Return all friends of a word.'''
    parts = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    adds = [a + c + b for a, b in parts for c in _Letters]
    removes = [a + b[1:] for a, b in parts if b]
    substitues = [a + c + b[1:] for a, b in parts for c in _Letters if b]
    return _Words & set(adds + removes + substitues)

word, unscanned, network, n, start = 'causes', set(), set(), 0, time.time()
while word:
    network.add(word)
    parts = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    adds = [a + c + b for a, b in parts for c in _Letters]
    removes = [a + b[1:] for a, b in parts if b]
    substitues = [a + c + b[1:] for a, b in parts for c in _Letters if b]
    unscanned |= (_Words & set(adds + removes + substitues)) - network
    word = unscanned.pop() if unscanned else ''
    n += 1
    if n % 10000 == 0:
        print '%5d %5.2f' % (len(unscanned), time.time() - start)
print len(network)
'''

word, unscanned, network, n, start = 'causes', set(), set(), 0, time.time()
while word:
    network.add(word)
    unscanned |= _friends(word) - network
    n += 1
    word = unscanned.pop() if unscanned else ''
    if n % 10000 == 0:
        print '%5d %5.2f' % (len(unscanned), time.time() - start)
print '%5d %5.2f' % (len(network), time.time() - start)
'''
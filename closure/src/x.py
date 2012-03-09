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
import xa
_Words = xa.Words
_Letters = 'abcdefghijklmnopqrstuvwxyz'

def suggestions(word):
    '''Return all one letter variants of a word.'''
    parts = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    adds = [a + c + b for a, b in parts for c in _Letters]
    removes = [a + b[1:] for a, b in parts if b]
    substitutes = [a + c + b[1:] for a, b in parts for c in _Letters if b]
    transposes = [a[:-1] + b[0] + a[-1] + b[1:] for a, b in parts if a and b]
    return _Words & set(adds + removes + substitutes + transposes)

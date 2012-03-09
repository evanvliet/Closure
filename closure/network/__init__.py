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
from one_character_misspelling_suggestions import suggestions

def count(word):
    unscanned, network = set(), set()
    while word:
        network.add(word)
        unscanned |= suggestions(word) - network
        word = unscanned.pop() if unscanned else ''
    return len(network)
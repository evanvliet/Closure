'''one character misspelling checker'''
import re
import string
import time
import logging
import dev_debug

_start = time.clock()
#from w1 import Words as Words
from words import Words as Words
logging.info('Words %.2f' % (time.clock() - _start))

#_Words = set([word.strip() for word in open('wlist.causes')])

def suggestions(word):
    '''Return all one letter variants of a word.'''
    # dev_debug.debug_break()
    parts = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    adds = [a + c + b for a, b in parts for c in string.lowercase]
    removes = [a + b[1:] for a, b in parts if b]
    substitutes = [a + c + b[1:] for a, b in parts for c in string.lowercase if b]
    transposes = [a[:-1] + b[0] + a[-1] + b[1:] for a, b in parts if a and b]
    return Words & set(adds + removes + substitutes + transposes)

if __name__ == '__main__':
    # test case
    print ', '.join(suggestions('able'))

import string
from words import Words as Words

#_Words = set([word.strip() for word in open('wlist.causes')])
_Letters = set('abcdefghijklmnopqrstuvwxyz')

def suggestions(word):
    '''Return all one letter variants of a word.'''
    if set(word) - _Letters:
        raise ValueError(''.join(set(word) - _Letters))
    parts = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    adds = [a + c + b for a, b in parts for c in _Letters]
    removes = [a + b[1:] for a, b in parts if b]
    substitutes = [a + c + b[1:] for a, b in parts for c in _Letters if b]
    transposes = [a[:-1] + b[0] + a[-1] + b[1:] for a, b in parts if a and b]
    return Words & set(adds + removes + substitutes + transposes)

if __name__ == '__main__':
    # test case
    print ', '.join(suggestions('able'))
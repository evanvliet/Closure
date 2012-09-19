import time
_all__ = ['home', 'find_words']
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import logging
import simplejson
from django.http import HttpResponse
from django.template import Context, loader
from google.appengine.ext import db
import dev_debug

_start = time.clock()
from ocms import Words
from collections import defaultdict
logging.info('Words %.2f' % (time.clock() - _start))
_start = time.clock()
word_data = defaultdict(list)
for i in Words:
    word_data[''.join(sorted(i))].append(i)
logging.info('word_data %.2f' % (time.clock() - _start))

class Anagram(db.Model):
    words = db.StringListProperty()

def home(request):
    return HttpResponse(
        loader.get_template(
            'index.html').render(Context({})))

def build(request):
    dev_debug.debug_break()
    n, _start = 0, time.time()
    _last = time.clock()
    _cutoff = time.time() + .1 * 60.0
    buf = []
    inc = 10
    for k in word_data:
        buf.append(Anagram(key_name=k, words=word_data[k]))
        if len(buf) > inc:
            db.put(buf)
            n_added = len(buf)
            n_lapsed = time.clock()
            lapsed_time = n_lapsed = _last
            _last = n_lapsed
            n_rate = n_added / n_lapsed
            n += n_added
            buf = []
            logging.info('%6d Anagrams %.2f' % (inc, n_rate))
            inc = min(1000, int(inc * 1.5))
        if time.time() > _cutoff:
            break
            
    n += len(db.put(buf))
    logging.info('%6d Anagrams %.2f' % (n, time.clock() - _last))
    json = simplejson.dumps({
                             'Anagrams': n,
                             'time': (time.time() - _start),
                             })
    return HttpResponse(json, mimetype='application/json')

def find_words(request, word=''):
    import ocms
    import string
    import re
    word = re.sub('[^a-z]', '', word.lower())
    anagram_signature = ''.join(sorted(word))
    anagram = word_data.get(anagram_signature, [])
    friends = ocms.suggestions(word)
    json = simplejson.dumps({
                             'for': word,
                             'words': anagram,
                             'suggestions': list(sorted(friends)),
                             })
    return HttpResponse(json, mimetype='application/json')



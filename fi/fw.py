_all__ = ['home', 'find_words']
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import logging
import simplejson
from django.http import HttpResponse
from django.template import Context, loader
from google.appengine.ext import db
import ocms
import dev_debug

from collections import defaultdict
word_data = defaultdict(list)
for i in ocms.Words:
    word_data[''.join(sorted(i))].append(i)

def canon(word):
    return sorted(word)

class Anagram(db.Model):
    words = db.StringListProperty()

def home(request):
    return HttpResponse(
        loader.get_template(
            'index.html').render(Context({})))

def find_words(request, word):
    # dev_debug.debug_break()
    anagram_signature = ''.join(sorted(word.lower()))
    anagram = word_data.get(anagram_signature, [''])
    friends = ocms.suggestions(word)
    json = simplejson.dumps({
                             'fw': anagram,
                             'ocms': list(sorted(friends))[:5],
                             })
    return HttpResponse(json, mimetype='application/json')


def suggest_words(request, word):
    friends = ocms.suggestions(word)
    json = simplejson.dumps(list(friends))
    return HttpResponse(json, mimetype='application/json')


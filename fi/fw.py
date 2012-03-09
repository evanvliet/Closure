_all__ = ['home', 'find_words']

import logging
import simplejson
from django.http import HttpResponse
from django.template import Context, loader
from google.appengine.ext import db

class Anagram(db.Model):
    words = db.StringListProperty()

def home(request):
    return HttpResponse(
        loader.get_template(
            'index.html').render(Context({})))

def find_words(request, word):
    anagram_signature = ''.join(sorted(word.upper()))
    anagram = Anagram.get_by_key_name(anagram_signature)
    matches = anagram.words if anagram else ['']
    json = simplejson.dumps(matches)
    return HttpResponse(json, mimetype='application/json')


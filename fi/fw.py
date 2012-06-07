_all__ = ['home', 'find_words']
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import simplejson
from django.http import HttpResponse
from django.template import Context, loader
import dev_debug
from anagrams import word_data

def home(request):
    return HttpResponse(
        loader.get_template(
            'index.html').render(Context({})))
    
def find_words(request, word):
    # dev_debug.debug_break()
    import ocms
    anagram_signature = ''.join(sorted(word.lower()))
    anagrams = word_data.get(anagram_signature, [''])
    friends = ocms.suggestions(word)
    json = simplejson.dumps({
                             'fw': anagrams,
                             'ocms': list(sorted(friends))[:5],
                             })
    return HttpResponse(json, mimetype='application/json')


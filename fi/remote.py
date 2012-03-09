#!/usr/bin/python
import code
import getpass
import sys, os, re

sys.path.append("/usr/local/google_appengine")
sys.path.append("/usr/local/google_appengine/lib")
sys.path.append("/usr/local/google_appengine/lib/simplejson")
sys.path.append("/usr/local/google_appengine/lib/django_0_96")
sys.path.append("/usr/local/google_appengine/lib/yaml/lib")

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext.db import GeoPt


# Hardwire in appengine modules to PYTHONPATH
# or use wrapper to do it more elegantly
#appengine_dirs = ['/Applications/blah/blah/google_appengine'...]
#sys.path.extend(appengine_dirs)
# Add your models to path
my_root_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, my_root_dir)

from fw import *

def auth_func():
    #return raw_input('Username:'), getpass.getpass('Password:')
    return 'vanvliet.eric', 'sd90sdlk'

if len(sys.argv) < 2:
    print "Usage: %s app_id [host]" % (sys.argv[0],)

app_id = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]
else:
    host = '%s.appspot.com' % re.sub(r's~', '', app_id)
print host

remote_api_stub.ConfigureRemoteDatastore(app_id, '/remote_api', auth_func, host)
code.interact('App Engine interactive console for %s' % (app_id,), None, locals())

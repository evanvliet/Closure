from django.conf.urls.defaults import *
import fw

urlpatterns = patterns('',
    (r'^words/(\w+)/$', fw.find_words),     
    # (r'^build/$', fw.build),
    (r'^$', fw.home),
)

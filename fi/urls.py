from django.conf.urls.defaults import *
import fw

urlpatterns = patterns('',
    (r'^words/(\w+)', fw.find_words),
    (r'^ocms/(\w+)', fw.suggest_words),
    (r'^$', fw.home),
)

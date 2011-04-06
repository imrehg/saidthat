from django.conf.urls.defaults import *

urlpatterns = patterns('stats.views',
    (r'^$', 'index'),
)

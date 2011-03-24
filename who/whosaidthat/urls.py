from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^whosaidthat/', include('whosaidthat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^api/', include('whosaidthat.api.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^puzzle/', include('whosaidthat.puzzle.urls')),
    (r'^p(\d*)/$', 'whosaidthat.puzzle.views.getpuzzle'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/dotcloud/current/static/'}),
)

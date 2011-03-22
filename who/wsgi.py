import os
import sys

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__)+"/whosaidthat")

os.environ['DJANGO_SETTINGS_MODULE'] = 'whosaidthat.settings'
import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)

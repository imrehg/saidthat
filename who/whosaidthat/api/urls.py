from django.conf.urls.defaults import *
from piston.resource import Resource
from whosaidthat.api.handlers import CategoryHandler, PersonHandler

class CsrfExemptResource(Resource):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )
        
category_handler = CsrfExemptResource(CategoryHandler)
person_handler = CsrfExemptResource(PersonHandler)

urlpatterns = patterns('',
   url(r'^category/add/', category_handler),
   url(r'^categories/', category_handler),
   url(r'^person/add/', person_handler),
)

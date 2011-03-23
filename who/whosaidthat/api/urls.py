from django.conf.urls.defaults import *
from piston.resource import Resource
from whosaidthat.api.handlers import CategoryHandler, PersonHandler, QuoteHandler

class CsrfExemptResource(Resource):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )
        
category_handler = CsrfExemptResource(CategoryHandler)
person_handler = CsrfExemptResource(PersonHandler)
quote_handler = CsrfExemptResource(QuoteHandler)

urlpatterns = patterns('',
   url(r'^category/add/', category_handler),
   url(r'^categories/', category_handler),
   url(r'^person/add/', person_handler),
   url(r'^quote/add/', quote_handler),
)

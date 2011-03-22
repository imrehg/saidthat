from django.conf.urls.defaults import *
from piston.resource import Resource
from whosaidthat.api.handlers import CategoryHandler

class CsrfExemptResource(Resource):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )
        
category_handler = CsrfExemptResource(CategoryHandler)

urlpatterns = patterns('',
   url(r'^category/add/', category_handler),
   url(r'^categories/', category_handler),
)

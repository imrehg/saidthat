from piston.handler import BaseHandler
from piston.utils import rc
from puzzle.models import Category
from django.db import IntegrityError

class CategoryHandler(BaseHandler):
   allowed_methods = ('GET', 'POST')
   model = Category
   fields = ('name', )

   def read(self, request):
       """ Return all the categories """
       return Category.objects.all()

   def create(self, request):
       """ Add new category """
       data = request.POST
       em = self.model(name=data['name'])
       try:
           em.save()
           resp = rc.CREATED
       except IntegrityError:
           resp = rc.DUPLICATE_ENTRY

       return resp
   

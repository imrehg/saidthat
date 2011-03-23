from piston.handler import BaseHandler
from piston.utils import rc
from puzzle.models import Category, Person, Quote
from django.db import IntegrityError
from django.template.defaultfilters import slugify
import simplejson as json
import email.utils
import datetime

def timeconvert(timestr):
    """Convert RFC 2822 defined time string into system timestamp"""
    timestamp = None
    timetuple = email.utils.parsedate_tz(timestr)
    if timetuple is not None:
        timestamp = email.utils.mktime_tz(timetuple)
    return timestamp

class CategoryHandler(BaseHandler):
   allowed_methods = ('GET', 'POST')
   model = Category
   fields = ('name', 'description', 'uri', )

   def read(self, request):
      """ Return all the categories """
      return Category.objects.all()
   
   def create(self, request):
       """ Add new category """
       data = request.POST
       em = self.model(name=data['name'],
                       slug=slugify(data['name']),
                       description=data['description'],
                       uri=data['uri'],
                       )
       try:
           em.save()
           resp = rc.CREATED
       except IntegrityError:
          resp = rc.DUPLICATE_ENTRY

       return resp
   
class PersonHandler(BaseHandler):
   allower_methods = ('POST',)
   model = Person
   category = Category

   def create(self, request):
      ## This is the way to get JSON
      data = json.loads(request.raw_post_data)

      em = self.model(name=data['name'],
                      screenname=data['screenname'],
                      description=data['description'],
                      imageurl=data['imageurl'],
                      url=data['url'],
                      verified=data['verified'],
                      location=data['location'],
                      twitterid=data['twitterid'],
                      )

      try:
         em.save()
         resp = rc.CREATED
      except IntegrityError:
         resp = rc.DUPLICATE_ENTRY

      ## Update category data
      person = Person.objects.filter(screenname=data['screenname'])[0]
      curr_cats = person.category.all()
      ccatnames = []
      for curr_cat in curr_cats:
         ccatnames += [curr_cat.name]
      ccatnames = set(ccatnames)
      incatnames = set(data['category'])
      ## Add what we don't have yet
      addnames = incatnames.difference(ccatnames)
      for addcat in addnames:
         cat_ref = Category.objects.filter(name=addcat)[0]
         person.category.add(cat_ref)
      ## Delete what does not exist anymore
      delnames = ccatnames.difference(incatnames)
      for delcat in delnames:
         cat_ref = Category.objects.filter(name=delcat)[0]
         person.category.remove(cat_ref)
      person.save()
      return resp

class QuoteHandler(BaseHandler):
   allower_methods = ('GET', 'POST',)

   def create(self, request):
      ## This is the way to get JSON
      data = json.loads(request.raw_post_data)
      author = data['user']['screen_name']
      person = Person.objects.filter(screenname=author)[0]
      posttime = datetime.datetime.fromtimestamp(timeconvert(data['created_at']))
      em = Quote(updateid=data['id'],
                 text=data['text'],
                 author=person,
                 posted=posttime
                 )
      try:
         em.save()
         resp = rc.CREATED
      except IntegrityError:
         resp = rc.DUPLICATE_ENTRY
      return resp

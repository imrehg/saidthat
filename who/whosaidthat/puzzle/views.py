from django.template import Context, loader
from puzzle.models import Quote, Person
from django.http import HttpResponse
import random

def index(request):
    # http://elpenia.wordpress.com/2010/05/11/getting-random-objects-from-a-queryset-in-django/
    count = Quote.objects.all().count()
    slice = int(random.random() * count)
    thisquote = Quote.objects.all()[slice]

    people = Person.objects.all().count()
    idlist = range(1, people+1)
    idlist.remove(thisquote.author.id)
    guess = random.sample(idlist, 3) + [thisquote.author.id]
    random.shuffle(guess)
    guesses = Person.objects.filter(id__in=guess)
    t = loader.get_template('puzzle/index.html')
    c = Context({
        'quote': thisquote,
        'guesses': guesses,
    })
    return HttpResponse(t.render(c))

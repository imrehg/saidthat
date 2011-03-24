from django.template import Context, RequestContext, loader
from puzzle.models import Quote, Person, Puzzle
from django.http import HttpResponse
import random
import simplejson as json
from django.shortcuts import render_to_response

def index(request):
    """ Create random puzzle """
    # http://elpenia.wordpress.com/2010/05/11/getting-random-objects-from-a-queryset-in-django/
    count = Quote.objects.all().count()
    slice = int(random.random() * count)
    thisquote = Quote.objects.all()[slice]

    ## PostgreSQL does not have consequitive IDs, so have to get them all
    idlist = [p.id for p in Person.objects.all()]
    authorid = thisquote.author.id
    idlist.remove(authorid)
    fakes = random.sample(idlist, 3)
    guess = fakes + [thisquote.author.id]
    random.shuffle(guess)
    guesses = Person.objects.filter(id__in=guess)
    fakepeeps = Person.objects.filter(id__in=fakes)
    newpuzzle = Puzzle(quote=thisquote,
                       fakeauth0=fakepeeps[0],
                       fakeauth1=fakepeeps[1],
                       fakeauth2=fakepeeps[2],
                       )
    newpuzzle.save()
    t = loader.get_template('puzzle/index.html')
    c = Context({
        'quote': thisquote,
        'guesses': guesses,
        'puzzle': newpuzzle,
    })
    return HttpResponse(t.render(c))

def showpuzzle(request, puzzle):
    guesses = [puzzle.quote.author, puzzle.fakeauth0, puzzle.fakeauth1, puzzle.fakeauth2]
    random.shuffle(guesses)
    data_dict = {
        'quote': puzzle.quote,
        'guesses': guesses,
        'puzzle': puzzle,
    }
    return render_to_response('puzzle/index.html', data_dict, context_instance=RequestContext(request))

def getpuzzle(request, number):
    """ Show puzzle or solution """
    if request.GET.get('solve', None) is not None:
        puzzlenum = number
        puzz = Puzzle.objects.filter(id=puzzlenum)
        if len(puzz) > 0:
            ret = puzz[0].quote.author.screenname
            out = {'author': ret}
            return HttpResponse(json.dumps(out))
        else:
            out = {'author': None}
            return HttpResponse(json.dumps(out))
    else:
        puzzlenum = number
        puzz = Puzzle.objects.filter(id=puzzlenum)
        if len(puzz) > 0:
            return showpuzzle(request, puzz[0])
        else:
            return HttpResponse("No such puzzle, dummy...")

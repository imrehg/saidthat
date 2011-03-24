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
    fakepeeps = Person.objects.filter(id__in=fakes)
    newpuzzle = Puzzle(quote=thisquote,
                       fakeauth0=fakepeeps[0],
                       fakeauth1=fakepeeps[1],
                       fakeauth2=fakepeeps[2],
                       )
    newpuzzle.save()
    return showpuzzle(request, newpuzzle)

def showpuzzle(request, puzzle):
    guesses = [puzzle.quote.author, puzzle.fakeauth0, puzzle.fakeauth1, puzzle.fakeauth2]
    random.shuffle(guesses)

    limit = 160
    header = "Who said:"
    puzzle_url = "http://who.saidth.at"+request.get_full_path()
    ballast = len(header)+40
    text = puzzle.quote.text
    if len(text)+ballast > limit:
        text = text[0:-(ballast+3)]+'...'
    puzzle_share_text = '%s "%s"' %(header, text)

    data_dict = {
        'quote': puzzle.quote,
        'guesses': guesses,
        'puzzle': puzzle,
        'puzzle_share_text': puzzle_share_text,
        'puzzle_url': puzzle_url,
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

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from puzzle.models import Person
import redis
from operator import itemgetter

def index(request):
    """ General stats display """
    redset = settings.REDIS
    r = redis.Redis(host=redset['host'],
                    port=redset['port'],
                    password=redset['password'],
                    )
    guess = dict(r.zrangebyscore("guess", "5", "+inf", withscores=True))
    guessgood = dict(r.zrangebyscore("goodguess", "0", "+inf", withscores=True))
    scores = []
    for person in guess:
        hits = guessgood.get(person, 0) / guess[person]
        scores += [(person, hits)]
    ranks = sorted(scores, key=itemgetter(1), reverse=True)
    # Get highest and lowest ranks
    bestguessed = Person.objects.filter(screenname=ranks[0][0])[0]
    bestguess = {
        "person" : bestguessed,
        "hit" : "%.2f" %(100*ranks[0][1])
        }
    worstguessed = Person.objects.filter(screenname=ranks[-1][0])[0]
    worstguess = {
        "person" : worstguessed,
        "hit" : "%.2f" %(100*ranks[-1][1])
        }

    data_dict = {
        "bestguess": bestguess,
        "worstguess": worstguess,
        }
    return render_to_response('stats/general.html', data_dict, context_instance=RequestContext(request))

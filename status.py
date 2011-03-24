import twitter
import twitter.oauth
import urllib
import urllib2
import simplejson as json
import re
from time import sleep

token = '269695642-V4K1i9luupSSDjlppgjiHTEFXDMiWqXVdZtbYX4g'
token_key = 'lP24WN5gfOkw55ain1f59rBOireovSvku9gRtUWs'
consumer_key = 'JHxS3cqx7hnS3RPQAXp6GQ'
consumer_secret = 'yqR9NuaF3V3SbnRbewWZHy8StrlnvUQhJ80sI1U'

# _BASE_URL = "http://localhost:8000"
_BASE_URL = "http://who.saidth.at"

tw = twitter.Twitter(auth=twitter.oauth.OAuth(token, token_key, consumer_key, consumer_secret))
# newstat = tw.statuses.friends_timeline(include_entities='t', count=200)
# for stat in newstat:
#     print stat['entities']

def update_categories():
    """ Create categories that we don't have yet """
    lists = tw.said_that_bot.lists()
    listnames = []
    for ll in lists['lists']:
        print ll['name'] + " : " + ll['description'] + " " + ll['slug']
        listnames += [(ll['name'], ll['slug'])]
        data = {'name': ll['name'],
                'description': ll['description'],
                'uri': ll['uri'],
                }
        qstring = urllib.urlencode(data)
        API_URL = "/api/category/add/"
        request = urllib2.Request(_BASE_URL+API_URL, qstring)
        results = None
        try:
            results = urllib2.urlopen(request).read()
        except:
            pass
    return listnames

def get_list_members(lists):
    people = {}
    for list in lists:
        func = getattr(tw.said_that_bot,list[1])
        members = func.members()['users']
        print "=== %s ===" %(list[0])
        for member in members:
            if people.get(member['screen_name'], None) is None:
                people[member['screen_name']] = {'screenname': member['screen_name'],
                                                 'name': member['name'],
                                                 # 'description': urllib.quote(member['description'].encode('utf8')),
                                                 'description': member['description'],
                                                 'imageurl': member['profile_image_url'],
                                                 'url': member['url'],
                                                 'verified': member['verified'],
                                                 'location': member['location'],
                                                 'twitterid': member['id'],
                                                 'category': [list[0]],
                                                 }
            else:
                people[member['screen_name']]['category'] += [list[0]]
    return people

def update_people(people):
    newpeople = []
    for person in people:
        query = json.dumps(people[person])
        headers = {'X_REQUESTED_WITH' :'XMLHttpRequest',
                   'ACCEPT': 'application/json, text/javascript, */*; q=0.01',}
        API_URL = "/api/person/add/"
        request = urllib2.Request(_BASE_URL+API_URL, query, headers)
        results = None
        try:
            results = urllib2.urlopen(request).read()
            # newpeople += [person]
        except:
            pass
        newpeople += [person]
        # break
        # sleep(1)
    return newpeople

def goodtweet(tweets):
    goodtweets = []
    url = re.compile(r"[\w\d&]+\.[\w\d&]+\.[\w\d&]{0,3}[^\w\d]+")
    mention = re.compile(r'\@[\w\d]+')
    for tweet in tweets:
        ### Working criteria!
        if ((len(tweet['entities']['urls']) == 0) and
            (len(tweet['entities']['user_mentions']) == 0) and
            (tweet['in_reply_to_status_id'] is None) and
            (url.search(tweet['text']) is None) and
            (mention.search(tweet['text']) is None)):
            goodtweets += [tweet]
            # print tweet['text']
    return goodtweets

def update_statuses(person):
    statlist = tw.statuses.user_timeline(screen_name=person, count=200, include_entities=1)
    goodlist = goodtweet(statlist)
    for stat in goodlist:
        query = json.dumps(stat)
        headers = {'X_REQUESTED_WITH' :'XMLHttpRequest',
                   'ACCEPT': 'application/json, text/javascript, */*; q=0.01',}
        API_URL = "/api/quote/add/"
        request = urllib2.Request(_BASE_URL+API_URL, query, headers)
        results = None
        try:
            results = urllib2.urlopen(request).read()
        except:
            pass
    return len(goodlist)
        
lists = update_categories()
list_data = get_list_members(lists)
newpeople = update_people(list_data)
for person in newpeople:
    updtd = update_statuses(person)
    print "%s: sent %d tweets" %(person, updtd)

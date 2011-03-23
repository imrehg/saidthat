import twitter
import twitter.oauth
import urllib
import urllib2
import simplejson as json

token = '269695642-V4K1i9luupSSDjlppgjiHTEFXDMiWqXVdZtbYX4g'
token_key = 'lP24WN5gfOkw55ain1f59rBOireovSvku9gRtUWs'
consumer_key = 'JHxS3cqx7hnS3RPQAXp6GQ'
consumer_secret = 'yqR9NuaF3V3SbnRbewWZHy8StrlnvUQhJ80sI1U'

_BASE_URL = "http://localhost:8000"

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
        # request = urllib2.Request(_BASE_URL+API_URL, qstring)
        # results = None
        # try:
        #     results = urllib2.urlopen(request).read()
        # except:
        #     print "Error"
        # print results
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
    for person in people:
        query = json.dumps(people[person])
        headers = {'X_REQUESTED_WITH' :'XMLHttpRequest',
                   'ACCEPT': 'application/json, text/javascript, */*; q=0.01',}
        API_URL = "/api/person/add/"
        request = urllib2.Request(_BASE_URL+API_URL, query, headers)
        results = None
        newpeople = []
        try:
            results = urllib2.urlopen(request).read()
            newpeople += [people]
        except:
            pass
    return newpeople

lists = update_categories()
list_data = get_list_members(lists)
newpeople = update_people(list_data)
print newpeople

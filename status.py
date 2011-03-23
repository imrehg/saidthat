import twitter
import twitter.oauth
import urllib
import urllib2

token = '269695642-V4K1i9luupSSDjlppgjiHTEFXDMiWqXVdZtbYX4g'
token_key = 'lP24WN5gfOkw55ain1f59rBOireovSvku9gRtUWs'
consumer_key = 'JHxS3cqx7hnS3RPQAXp6GQ'
consumer_secret = 'yqR9NuaF3V3SbnRbewWZHy8StrlnvUQhJ80sI1U'

tw = twitter.Twitter(auth=twitter.oauth.OAuth(token, token_key, consumer_key, consumer_secret))
# newstat = tw.statuses.friends_timeline(include_entities='t', count=200)
# for stat in newstat:
#     print stat['entities']

def update_categories():
    """ Create categories that we don't have yet """
    lists = tw.said_that_bot.lists()
    for ll in lists['lists']:
        print ll['name'] + " : " + ll['description'] + " " + ll['slug']
        data = {'name': ll['name'],
                'description': ll['description'],
                'uri': ll['uri'],
                }
        qstring = urllib.urlencode(data)
        _BASE_URL = "http://who.saidth.at/api/category/add/"
        request = urllib2.Request(_BASE_URL, qstring)
        results = None
        try:
            results = urllib2.urlopen(request).read()
        except:
            print "Error"
        print results


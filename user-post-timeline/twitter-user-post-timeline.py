import tweepy
from tweepy import OAuthHandler
import json

def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

api = load_api()
user = 'spuryyc'
tweets = api.user_timeline(id=user, count=1000)
print('Found %d tweets' % len(tweets))

# You now have a list of tweet objects with various attributes
# check out the structure here: http://tkang.blogspot.ca/2011/01/tweepy-twitter-api-status-object.html

# For example we can get the text of each tweet
tweets_text = [t.text for t in tweets]
filename = 'tweets-'+user+'.json'
json.dump(tweets_text, open(filename, 'w'))
print('Saved to file:', filename)

# Can load file like this
#tweets_text = json.load(open(filename, 'r'))

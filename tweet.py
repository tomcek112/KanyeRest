import tweepy
from tweepy import OAuthHandler
from pymarkovchain import MarkovChain
import requests, time
import re
r = requests.get('http://www.kanyerest.xyz/api/lyrics')
#print r.content


consumer_key = 'ZdOfyIbTOauE15k2LChIE09du'
consumer_secret = 'XhAa1HUqU6oYieH746KAcICw8oRbOqtpxMOSXMUun724pRnJhU'
access_token = '706117375863689217-jPUo2aw3r8mSYKzpWIirm2b9KpPA8nN'
access_secret = 'H0nCKygT1RybhSmrwKCtkP6koZFKJzPfUabTssGURIPoL'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

yeezy = tweepy.API(auth)

def getLines():
	mc = MarkovChain("")
	mc.generateDatabase(r.content)
	tweet = mc.generateString()
	tweet = tweet[:140].rsplit(r'\n', 1)[0]
	return tweet

def postTweet():
	tweet = getLines()
	yeezy.update_status(status=tweet)


print postTweet()




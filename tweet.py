import tweepy
from tweepy import OAuthHandler
from pymarkovchain import MarkovChain
import requests, time
import re
from daemon import runner 

r = requests.get('http://www.kanyerest.xyz/api/lyrics')
#print r.content


consumer_key = 'CONSUMER-KEY'
consumer_secret = 'CONSUMER-SECRET'
access_token = 'ACCESS-TOKEN'
access_secret = 'ACCESS-SECRET'

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




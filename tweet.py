from pymarkovchain import MarkovChain
import requests, time
r = requests.get('http://www.kanyerest.xyz/api/all')
#print r.content



mc = MarkovChain("")
mc.generateDatabase(r.content)
tweet = mc.generateString()
tweet = tweet[:140].rsplit(' ', 1)[0]
print(tweet)



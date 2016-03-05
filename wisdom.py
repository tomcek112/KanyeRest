import tweepy
from tweepy import OAuthHandler
from pymarkovchain import MarkovChain
import requests, time
import re

def writeLine():
	r = requests.get('http://www.kanyerest.xyz/api/lyrics')
	mc = MarkovChain("")
	mc.generateDatabase(r.content)
	tweet = mc.generateString()
	tweet = tweet[:140].rsplit(r'\n', 1)[0]
	return tweet

def wisdom():
	arr1 = []
	arr2 = []
	arr2Lasts = []
	arr1Lasts = []
	res=[]
	arr1.append(writeLine())
	arr1Lasts.append(arr1[0][-2:])
	for i in range(0,30):
		car = writeLine()
		arr2.append(car)
		arr2Lasts.append(car[-2:])
	# if (line[:-1] == line2[:-1]):
	# 	arr.append(line)
	# 	arr.append(line2)
	# 	return arr
	# else:
	# 	wisdom()
	# print(str(arr1))
	# print(str(arr2))
	# print(str(arr2Lasts))
	# print(str(arr1Lasts))
	i = 0
	while(i < 29):
		if arr2Lasts[i] == arr1Lasts[0]:
			res.append(arr2[i])
			res.append(arr1[0])
			return res
		i += 1
	
	wisdom()


# bla = wisdom()
# print('------------------------------------------------------------------------------------------------')
# print str(bla)
# blo = wisdom()
# print('------------------------------------------------------------------------------------------------')
# print str(blo)

# print('###########')
# print(str(blo))
# print(str(bla))

def song():
	arr = []
	for i in range(0,4):
		line = wisdom()
		line2 = wisdom()
		arr.append(line)
		arr.append(line2)

	return arr

arr = song()
for a in arr:
	if a:
		print(a[0])
		print(a[1])

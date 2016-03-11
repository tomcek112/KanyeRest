from songer import MarkovChain
import requests, time
import re
from markov import genSentence

# r = requests.get('http://www.kanyerest.xyz/api/lyrics')
# mc = MarkovChain("")
# mc.generateDatabase(r.content)


def writeLine():
	tweet = genSentence()
	return tweet

def createRhymePair():
	song = []
	line1 = genSentence()[:-1]
	line2 = genSentence()[:-1]
	while line2[-2:] != line1[-2:]:
		line1 = genSentence()[:-1]
		line2 = genSentence()[:-1]
	song.append(line1)
	song.append(line2)
	return song

def createRhymePair2():
	lines = []
	pair = []
	for i in range(0, 9):
		lines.append(genSentence()[:-1])
	comp_line = genSentence()[:-1]
	while not pair:
		for line in lines:
			if line[:-2] == comp_line[:-2]:
				pair.append(line)
				pair.append(comp_line)
				return pair


def createSong(n):
	song = []
	for i in range(0,n-1):
		song.append(createRhymePair())
	return song

def printSong(n):
	lyrics = []
	for line in createSong(n):
		lyrics.append(line[0])
		lyrics.append(line[1])
	return lyrics



def createSonger():
	song = []
	match = []
	i=0
	matches=[]
	while(i<8):
		song.append(writeLine())
		i += 1 
	
	pieces = []

	for wis in song:
		wis = wis[:-1]
		pieces.append(wis[-2:])


	match = [x for x in pieces if pieces.count(x) >= 2]
	
	a=0
	if match:
		while(a<8):
			if(song[a][-3:-1] == match[0]):
				matches.append(song[a])
			a += 1

	return matches


#print createSonger()
def createLongSonger():
	meh = []
	i = 0
	while(len(meh)<8):
		muh = createSonger()
		if muh:
			#print(muh)
			meh.append(muh[0])
			meh.append(muh[1])
		i += 1
	return meh


# print('########################################')

# #print(str(meh))
# for o in meh:
# 	print o



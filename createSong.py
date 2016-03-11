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

print createRhymePair()

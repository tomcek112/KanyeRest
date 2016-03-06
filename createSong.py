from songer import MarkovChain
import requests, time
import re

r = requests.get('http://www.kanyerest.xyz/api/lyrics')
mc = MarkovChain("")
mc.generateDatabase(r.content)


def writeLine():
	tweet = mc.generateString()
	tweet = tweet[:140].rsplit(r'\n', 1)[0]
	return tweet

def createRhymePair():
	song = []
	line1 = re.sub(r'\)|\(', '', writeLine())
	song.append(line1)
	line2 = re.sub(r'\)|\(', '', writeLine())
	while line2[-2:] != line1[-2:]:
		line2 = re.sub(r'\)|\(', '', writeLine())
	song.append(line2)
	return song


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


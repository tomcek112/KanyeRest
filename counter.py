import requests, time
import re

def writeLine():
	r = requests.get('http://www.kanyerest.xyz/api/lyrics')
	arr = r.content.split(' ')
	print arr

writeLine()
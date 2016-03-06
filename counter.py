import requests, time
import re

def writeLine():
	r = requests.get('http://www.kanyerest.xyz/api/lyrics')
	arr = r.content.split(' ')
	j = {}
	for x in arr:
		if not j[x]:
			j[x] = j.count(x)
	return jsonify(j)

writeLine()
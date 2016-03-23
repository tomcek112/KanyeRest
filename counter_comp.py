import requests
import json
import re


def writeLine():
	r = requests.get('http://www.kanyerest.xyz/api/lyrics')
	r = r.content
	r = re.sub('\!', '', r)
	r = re.sub('\.', '', r)
	r = re.sub('\,', '', r)
	r = re.sub('\?', '', r)
	r = re.sub('\;', '', r)
	r = re.sub('\'', '', r)
	r = re.sub('\(', '', r)
	r = re.sub('\)', '', r)
	r = re.sub('\"', '', r)
	r = re.sub('\[', '', r)
	r = re.sub('\]', '', r)
	r = re.sub('\-', ' ', r)
	r = r.lower()
	arr = r.split(' ')
	unsorted = {}
	for x in arr:
		unsorted[x] = arr.count(x)
	# sorted2 = sorted(sorted2, key=unsorted.get)
	# #sorted2 = sorted2[::-1]
	# sorted3 = {}
	# for x in sorted2:
	# 	sorted3[x] = unsorted[x]
	print unsorted


writeLine()

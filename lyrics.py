# import urllib
# import sys
# import subprocess
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import time
import re
import lxml.html



base_url = "http://lyrics.wikia.com"
yeezys_page = "http://lyrics.wikia.com/wiki/Kanye_West"
test_url = "http://lyrics.wikia.com/wiki/Jay-Z_%26_Kanye_West:Niggas_In_Paris"

# def getAlbum(url):
# 	doc = lxml.html.parse(url)
# 	#albumSen = doc.getroot().cssselect("")
# 	wholepage = fromstring(doc)
# 	for yeezy in wholepage.find_all(['<a href="/wiki']):
# 		print yeezy



def getLyrics(url):
	doc = lxml.html.parse(url)
	kanyes = doc.getroot().cssselect(".lyricbox")[0]
	lyrics = []
	if kanyes.text is not None:
		lyrics.append(kanyes.text)
	for kanye in kanyes:
		if str(kanye.tag).lower() == "br":
			lyrics.append("\n")
		if kanye.tail is not None:
			lyrics.append(kanye.tail)
	full = "".join(lyrics).strip()
	return full


def getAllLyrics():
	lyrics = []
	links = []
	source_code = requests.get(yeezys_page)
	plain_text = source_code.text.encode("utf-8")
	soupeezy = BeautifulSoup(plain_text, 'html.parser')
	for yeezy in soupeezy.select('ol > li > b > a'):
		link = urljoin(base_url, yeezy['href'])
		links.append(link)
	for i in range(0,10):
	  	lyrics.append(getLyrics(link))
	   	time.sleep(1)
	return lyrics[0]



print getAllLyrics()
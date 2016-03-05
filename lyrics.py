
# import urllib
# import sys
# import subprocess
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import time
import re
import lxml.html
from pymongo import MongoClient


base_url = "http://lyrics.wikia.com"
yeezys_page = "http://lyrics.wikia.com/wiki/Kanye_West"
test_url = "http://lyrics.wikia.com/wiki/Kanye_West:Big_Brother"


client = MongoClient()
db = client.kanye

def getTitle(url):
	source_code = requests.get(url)
	plain_text = source_code.text.encode("utf-8")
	soupeezy = BeautifulSoup(plain_text, 'html.parser')
	meta_title = soupeezy.title.string
	meta_title = re.sub(r'(Kanye West).*\:', "", meta_title)
	title = re.sub(r'( Lyrics - LyricWikia - Wikia)', "", meta_title)
	title = re.sub(" ", "_", title)
	return title

def getAlbum(url):
	source_code = requests.get(url)
	plain_text = source_code.text.encode("utf-8")
	soupeezy = BeautifulSoup(plain_text, 'html.parser')
	album_html = str(soupeezy.select('p > i > a'))
	album_html = re.sub(r"(\w|\s|\W)*\"\s(title)\=\"(\w|\s|\W)*\"\>", "", album_html)
	album = re.sub(r"\s\((\d){4}\)\<\/a\>\]", "", album_html)
	album = re.sub(" ", "_", album)
	return album

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
	result = db.kanye.insert_one({
			"title": getLyrics(url),
			"album": getAlbum(url),
			"lyrics": str(full)
		})
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
	  	lyrics.append(getLyrics(links[i]))
	   	time.sleep(1)
	return lyrics[0]




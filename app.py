import os
import math
from flask import Flask, jsonify, render_template, request, session, g, redirect, url_for, abort, flash, make_response
import requests
import json
from pymongo import MongoClient
from bson import json_util
import lyrics as lyrics
# from createSong import printSong




app = Flask(__name__)
app.config.from_object(__name__)

client = MongoClient()
db = client.kanye


@app.route('/')
def index():
	print('YEEZY')
	return render_template('index.html')


@app.route('/api/track/<name>')
def title(name):
	cur = db.kanye.find({"title": name})
	if cur:
		for doc in cur:
			doc.pop("_id", None )
			return jsonify(doc)

	return jsonify(title= None, year=None, album=None, lyrics=None), 404

@app.route('/api/album/<name>')
def album(name):
	cur = db.kanye.find({"album": name})
	ret = {'result': []}
	for doc in cur:
		doc.pop("_id", None)
		ret['result'].append(doc)
	if ret:
		return jsonify(ret)
	else:
		return jsonify(title= None, year=None, album=None, lyrics=None), 404


@app.route('/api/all')
def all():
	cur = db.kanye.find()
	ret = []
	for doc in cur:
		doc.pop("_id", None)
		ret.append(doc)
	if ret:
		return json.dumps(ret)
	else:
		return jsonify(title= None, year=None, album=None, lyrics=None), 404

@app.route('/api/lyrics')
def lyr():
        cur = db.kanye.find()
        ret = []
        i = 0
        for doc in cur:
                doc.pop("_id", None)
                ret.append(doc)
        returner = ""
        for track in ret:
                returner += track['lyrics']
        if ret:
                return returner
        else:
                return jsonify(title= None, year=None, album=None, lyrics=None), 404


@app.route('/docs')
def docs():
	print('YEEZY')
	return render_template('docs.html')

@app.route('/about')
def about():
	print('YEEZY')
	return render_template('about.html')

@app.route('/kd')
def kd():
	print('YEEZY')
	return render_template('kd.html')

def fun():
	r = requests.get('http://www.kanyerest.xyz/api/lyrics')
	arr = r.content.lower().split(' ')
	se = set(arr)
	j = {}
	for x in se:
		j[x] = arr.count(x)
	return j

# @app.route('/serenade')
# def serderderder():
# 	print('test')
# 	c = printSong(8)
# 	return render_template('serenade.html', c=c)

@app.route('/api/counter')
def writeLine():
	print('YEEZY')
	r = requests.get('http://www.kanyerest.xyz/static/counter.json')
	b = r.json()
	return jsonify(b)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404





if __name__ == '__main__':
    app.run(debug=True)





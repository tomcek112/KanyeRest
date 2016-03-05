import os
import math
from flask import Flask, jsonify, render_template, request, session, g, redirect, url_for, abort, flash, make_response
import requests
import json
from pymongo import MongoClient
from bson import json_util
import lyrics as lyrics




app = Flask(__name__)
app.config.from_object(__name__)

client = MongoClient()
db = client.kanye
# result = db.kanye.insert_one(
# 		{
# 			"title": "test",
# 			"year": "test",
# 			"album": "test",
# 			"lyrics": "bla bla bla"

# 		}
# 	)

# result = db.kanye.insert_one(
# 		{
# 			"title": "test 2",
# 			"year": "test 2",
# 			"album": "test",
# 			"lyrics": "bla bla bla"

# 		}
# 	)
# coolStuff = db.kanye.find()
# arr = []

# for doc in coolStuff:
# 	arr.append(doc)


# foo = db.kanye.find({"title": "test"})
# for d in foo:
# 	print(type(d))
# 	print d

#db.kanye.drop()

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

if __name__ == '__main__':
    app.run(debug=True)

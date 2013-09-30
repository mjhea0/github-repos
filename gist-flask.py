import os
import requests
from requests.auth import HTTPBasicAuth
import simplejson
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
app.config.from_object('config')


def showUserGists(username):
	gists = []
	r = requests.get(('https://api.github.com/users/%s/repos?type=owner&per_page=100' % username), auth=HTTPBasicAuth('mjhea0', app.config['PASSWORD']))

	c = r.content
	j = simplejson.loads(c)
	for item in j:
		gists.append(item['html_url'])
	return gists

@app.route('/')
def hi():
	students = ["afantinelli", "BrianKoester", "cmlizama", "kcraig01", "imjessw", "gemfarmer", "spacebug808", "sapientsaphead", "wheresmypen", "mjhea0", "jennvance", "rserota", "jdaudier", "lori-bogart", "Devaio", "yalcindo", "juliebarsi", "mmckelvy", "ralucas"]

	gists = []
	new = []
	for student in students:
		new.append(showUserGists(student))
	for x in (new):
		for y in x:
			if "refactor" in y.lower():
				gists.append(y)
	return render_template('results.html', gists=gists)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000,))
	app.debug = False
	app.run(host='0.0.0.0', port=port)

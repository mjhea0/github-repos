import os
import requests
from requests.auth import HTTPBasicAuth
import simplejson

from flask import Flask, render_template

# config
app = Flask(__name__)
app.config.from_object('config')


# helper functions

def get_repos(username):
    """
    Given a username, this function returns
    all repos associated with that username.
    """
    repos = []
    r = requests.get(
        ('https://api.github.com/users/{}/repos?type=owner&per_page=100'
            .format(username)),
        auth=HTTPBasicAuth('mjhea0', app.config['PASSWORD'])
    )
    c = r.content
    j = simplejson.loads(c)
    for item in j:
        repos.append(item['html_url'])
    return repos


# routes

@app.route('/')
def hi():
    """
    Grad all repos from a student, add repo to final
    list of repos if a certain keyword is present.
    """
    students = ["mjhea0"]  # add list of Guthub accounts
    repos = []
    new = []
    for student in students:
        new.append(get_repos(student))
    for x in (new):
        for y in x:
            if "refactor" in y.lower():
                repos.append(y)
    return render_template('results.html', repos=repos)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000,))
    app.debug = False
    app.run(host='0.0.0.0', port=port)

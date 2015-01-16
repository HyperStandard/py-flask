import os
from datetime import datetime

from flask import Flask, render_template, send_from_directory, g, request
import sqlite3
from api import PyFlaskApi
from database import DataBase

from links import Link

from collections import OrderedDict

app = Flask(__name__)

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True
    print("Running server on OpenShift")

if not ON_OPENSHIFT:
    print("Running server  locally, app.testing = True")
    app.debug = True

app.config.from_pyfile('flaskapp.cfg')


def inject_links():
    # return OrderedDict({"main": "/", "about": "/about", "sanity check": "/sanity" })
    return (
        Link("main", "/"),
        Link("about", "/about"),
        Link("sanity check", "/sanity"))
    #return ("main", "/"), ("about", "/about"), ("sanity check", "/sanity")


app.jinja_env.globals['navlinks'] = inject_links
app.jinja_env.globals['today'] = datetime.today
app.jinja_env.globals['len'] = len

@app.before_first_request
def app_startup():
    g.app_database = DataBase()


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.route("/test")
def test():
    return render_template("ajaxtest.html")

@app.route("/sanity")
def sanity():
    return "I'm sane 🌹"


@app.route("/dev")
def dev():
    return render_template("links.html")

@app.route("/api/<api_call>/<value>")
def call_api(api_call, value):
    if api_call is "data":
        return PyFlaskApi.get_data(value)
    elif api_call is "user":
        return PyFlaskApi.get_user(value)
    else:
        return "error, unknown api call"

@app.route("/api/submit", methods=['POST'] )
def post_submit_data():
    message = request.form['message']
    print(message + ":message")
    get_db().add_to_db(message, "whateber")
    return message



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def db_connect():
    return sqlite3.connect('assets/items.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DataBase()
    return db

if __name__ == '__main__':
    app.run()

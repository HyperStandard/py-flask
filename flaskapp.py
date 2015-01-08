import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from flask.ext.scss import Scss
from jinja2 import Template

app = Flask(__name__)

#instantiate Sccs object when runs Scss compiling
Scss(app, static_dir='static', asset_dir='assets')

app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/test2")
def test2():
    return render_template("base.html")

@app.route("/sanity")
def sanity():
    return "1"

@app.route("/dev")
def dev():
    return render_template("links.html", links=inject_links())
    #links = (("main", "/"), ("about", "/about"), ("sanity check", "/sanity"))
    #template = Template(test.html)
    #return template.render(link=links)

@app.context_processor
def inject_links():
    return (("main", "/"), ("about", "/about"), ("sanity check", "/sanity"))

if __name__ == '__main__':
    app.run()

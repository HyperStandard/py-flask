import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from flask.ext.scss import Scss

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

if __name__ == '__main__':
    app.run()

import os
from datetime import datetime

from flask import Flask, render_template, send_from_directory

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
    return ("main", "/"), ("about", "/about"), ("sanity check", "/sanity")

app.jinja_env.globals['navlinks'] = inject_links
app.jinja_env.globals['today'] = datetime.today

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
    return "I'm sane 🌹"

@app.route("/dev")
def dev():
    return render_template("links.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run()

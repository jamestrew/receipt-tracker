import flask

from receipt_tracker.flask import app


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route("/stats")
def stats():
    return flask.render_template('stats.html')
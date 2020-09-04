import flask

from receipt_tracker.flask import app, db
from receipt_tracker.flask.forms import ClientForm
from receipt_tracker.repo.models import Buyer


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route("/stats")
def stats():
    return flask.render_template('stats.html')


@app.route("/new_client", methods=['GET', 'POST'])
def new_client():
    form = ClientForm()

    if form.validate_on_submit():
        client = Buyer(name=form.name.data)
        db.add(client)
        db.commit()
        flask.flash(f'New buyer {form.name.data} added!', 'success')
        return flask.redirect(flask.url_for('home'))

    return flask.render_template('new_client.html', form=form)

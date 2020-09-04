import flask

from receipt_tracker.flask import app, db
from receipt_tracker.flask.forms import ClientForm, BusinessForm
from receipt_tracker.repo.models import Buyer, Seller


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route("/stats")
def stats():
    return flask.render_template('stats.html')


@app.route("/add_new", methods=['GET', 'POST'])
def add_new():
    client_form = ClientForm()
    business_form = BusinessForm()

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form)


@app.route("/add_client", methods=['GET', 'POST'])
def add_client():
    client_form = ClientForm()
    business_form = BusinessForm()

    if client_form.validate_on_submit():
        client = Buyer(name=client_form.client_name.data)
        db.add(client)
        db.commit()
        flask.flash(f'New buyer {client_form.client_name.data} added!', 'success')
        # return flask.redirect(flask.url_for('home'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form)


@app.route("/add_business", methods=['GET', 'POST'])
def add_business():
    client_form = ClientForm()
    business_form = BusinessForm()

    if business_form.validate_on_submit():
        seller = Seller(name=business_form.business_name.data)
        db.add(seller)
        db.commit()
        flask.flash(f'New seller {business_form.business_name.data} added!', 'success')
        # return flask.redirect(flask.url_for('home'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form)

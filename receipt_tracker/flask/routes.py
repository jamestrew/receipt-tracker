import flask
import json

from receipt_tracker.flask import app, db
from receipt_tracker.flask.forms import ClientForm, BusinessForm, ReceiptForm
from receipt_tracker.repo.models import Buyer, Seller, Receipt


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route("/stats")
def stats():
    print(get_buyers(), '\n')
    print(get_sellers(), '\n')
    print([receipt for receipt in Receipt.query.all()])
    return flask.render_template('stats.html')


@app.route("/add_new", methods=['GET', 'POST'])
def add_new():
    client_form = ClientForm()
    business_form = BusinessForm()
    receipt_form = ReceiptForm()

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form,
                                 receipt_form=receipt_form
                                 )


@app.route("/add_client", methods=['GET', 'POST'])
def add_client():
    client_form = ClientForm()
    business_form = BusinessForm()
    receipt_form = ReceiptForm()

    if client_form.validate_on_submit():
        client = Buyer(name=client_form.client_name.data)
        db.add(client)
        db.commit()
        flask.flash(f'New buyer {client_form.client_name.data} added!', 'success')
        return flask.redirect(flask.url_for('add_new'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form,
                                 receipt_form=receipt_form
                                 )


@app.route("/add_business", methods=['GET', 'POST'])
def add_business():
    client_form = ClientForm()
    business_form = BusinessForm()
    receipt_form = ReceiptForm()

    if business_form.validate_on_submit():
        seller = Seller(name=business_form.business_name.data)
        db.add(seller)
        db.commit()
        flask.flash(f'New seller {business_form.business_name.data} added!', 'success')
        return flask.redirect(flask.url_for('add_new'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form,
                                 receipt_form=receipt_form
                                 )


@app.route("/add_receipt", methods=['GET', 'POST'])
def add_receipt():
    client_form = ClientForm()
    business_form = BusinessForm()
    receipt_form = ReceiptForm()

    if receipt_form.validate_on_submit():
        buyer = Buyer.query.filter_by(name=receipt_form.buyer.data).first()
        seller = Seller.query.filter_by(name=receipt_form.seller.data).first()
        receipt = Receipt(date=receipt_form.date.data,
                          buyer_id=buyer.id,
                          seller_id=seller.id,
                          total=receipt_form.total.data,
                          description=receipt_form.description.data
                          )
        db.add(receipt)
        db.commit()
        flask.flash(f'New receipt added!', 'success')
        return flask.redirect(flask.url_for('add_new'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form,
                                 receipt_form=receipt_form
                                 )


def get_buyers():
    return [buyer.name for buyer in Buyer.query.all()]


def get_sellers():
    return [seller.name for seller in Seller.query.all()]


@app.route('/_autocomplete_buyer', methods=['GET'])
def autocomplete_buyer():
    return flask.Response(json.dumps(get_buyers()), mimetype='application/json')


@app.route('/_autocomplete_seller', methods=['GET'])
def autocomplete_seller():
    return flask.Response(json.dumps(get_sellers()), mimetype='application/json')

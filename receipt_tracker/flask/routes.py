import flask
import json

from receipt_tracker.flask import app, repo, session
from receipt_tracker.flask.forms import ClientForm, BusinessForm, ReceiptForm
from receipt_tracker.repo.models import Buyer, Seller, Receipt
from receipt_tracker.use_cases import list_uc


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route("/stats")
def stats():
    # Temporary prints for debugging
    print(list_uc.GetNames(repo, Buyer).execute(), '\n')
    print(list_uc.GetNames(repo, Seller).execute(), '\n')
    print([receipt for receipt in Receipt.query.all()])
    return flask.render_template('stats.html')


@app.route("/add_new", methods=['GET', 'POST'])
def add_new():
    """
    Main route to page for all three buyer, seller, receipt add forms.

    Implemented using first solution by Grey Li (Update version).
    See: https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms

    """
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
        session.add(client)
        session.commit()
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
        session.add(seller)
        session.commit()
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
        session.add(receipt)
        session.commit()
        flask.flash(f'New receipt added!', 'success')
        return flask.redirect(flask.url_for('add_new'))

    return flask.render_template('add_new.html',
                                 client_form=client_form,
                                 business_form=business_form,
                                 receipt_form=receipt_form
                                 )


@app.route('/_autocomplete_buyer', methods=['GET'])
def autocomplete_buyer():
    """Helper route for jQuery autocomplete function."""
    return flask.Response(json.dumps(list_uc.GetNames(repo, Buyer).execute()),
                          mimetype='application/json')


@app.route('/_autocomplete_seller', methods=['GET'])
def autocomplete_seller():
    """Helper route for jQuery autocomplete function."""
    return flask.Response(json.dumps(list_uc.GetNames(repo, Seller).execute()),
                          mimetype='application/json')

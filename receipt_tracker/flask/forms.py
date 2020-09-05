import datetime

from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from receipt_tracker.repo.models import Buyer, Seller


class ClientForm(FlaskForm):

    client_name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Add User')

    def validate_client_name(self, client_name):
        """Ensure client_name is unique."""
        buyer = Buyer.query.filter_by(name=client_name.data).first()
        if buyer:
            raise ValidationError('Buyer already exists.')


class ReceiptForm(FlaskForm):

    buyer = StringField('Buyer Name', validators=[DataRequired()], id='buyer')
    seller = StringField('Seller Name', validators=[DataRequired()], id='seller')
    date = DateField('Sale Date', validators=[DataRequired()])
    total = FloatField('Purchase Total', validators=[DataRequired()])
    description = StringField('Short Description')
    submit = SubmitField('Add Receipt')

    def validate_date(self, date):
        """Ensure date entered is in the past."""
        if date.data > datetime.date.today():
            raise ValidationError('Sale date must be in the past.')

    def validate_buyer(self, buyer):
        """Ensure buyer exists."""
        entity = Buyer.query.filter_by(name=buyer.data).first()
        if entity is None:
            raise ValidationError('Buyer does not exist.')

    def validate_seller(self, seller):
        """Ensure seller exists."""
        entity = Seller.query.filter_by(name=seller.data).first()
        if entity is None:
            raise ValidationError('Seller does not exist.')


class BusinessForm(FlaskForm):

    business_name = StringField('Business Name', validators=[DataRequired()])
    submit = SubmitField('Add Seller')

    def validate_business_name(self, business_name):
        """Ensure business_name is unique."""
        seller = Seller.query.filter_by(name=business_name.data).first()
        if seller:
            raise ValidationError('Seller already exists.')

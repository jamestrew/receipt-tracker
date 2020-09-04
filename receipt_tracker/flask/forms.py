from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from receipt_tracker.repo.models import Buyer


class ClientForm(FlaskForm):

    name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Add User')

    def validate_name(self, name):
        buyer = Buyer.query.filter_by(name=name.data).first()
        if buyer:
            raise ValidationError('Buyer already exists.')


class ReceiptForm(FlaskForm):

    date = DateField('Sale Date', validators=[DataRequired()])
    total = FloatField('Purchase Total', validators=[DataRequired()])
    description = StringField('Short Description')
    submit = SubmitField('Add Receipt')


class BusinessForm(FlaskForm):

    name = StringField('Business Name', validators=[DataRequired()])
    submit = SubmitField('Add Seller')

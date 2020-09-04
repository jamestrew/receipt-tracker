from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):

    name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Add User')


class ReceiptForm(FlaskForm):

    date = DateField('Sale Date', validators=[DataRequired()])
    total = FloatField('Purchase Total', validators=[DataRequired()])
    description = StringField('Short Description')
    submit = SubmitField('Add Receipt')


class BusinessForm(FlaskForm):

    name = StringField('Business Name', validators=[DataRequired()])
    submit = SubmitField('Add Seller')

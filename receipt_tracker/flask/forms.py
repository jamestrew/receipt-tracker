import datetime

from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, PasswordField,
                     StringField, SubmitField)
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from receipt_tracker.repo.models import Buyer, Seller, User


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
    date = DateField('Sale Date', validators=[DataRequired()], render_kw={"placeholder": "yyyy-mm-dd"})
    total = FloatField('Purchase Total', validators=[DataRequired()], render_kw={"aria-label": "Amount  (to the nearest dollar)"})
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


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

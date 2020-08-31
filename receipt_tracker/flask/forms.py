from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class PersonForm(FlaskForm):

    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add User')


class ReceiptForm(FlaskForm):

    total = FloatField('Purchase Total', validators=[DataRequired()])
    description = StringField('Short Description')
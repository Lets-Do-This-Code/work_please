from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class NewOrderForm(FlaskForm):
    driver = SelectField('Driver', choices=[], coerce=int) 
    ordernum = StringField('Order #', validators=[DataRequired()])
    custname = StringField('Cust Name', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    suburb = StringField('Suburb', validators=[DataRequired()])
    submit = SubmitField('Place Order')

class EditOrderForm(FlaskForm):
    orderID = StringField('Order #', validators=[DataRequired()])
    driver = SelectField('Driver', choices=[], coerce=int) 
    name = StringField('Cust Name', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    suburb = StringField('Suburb', validators=[DataRequired()])
    submit = SubmitField('Update Order')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register Order')





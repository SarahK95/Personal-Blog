from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, length
from ..models import User
from wtforms import ValidationError


class SignUpForm(FlaskForm):
    username = StringField(validators={InputRequired(),length(min=3,
         max=10)},render_kw={"placeholder":"Enter Username"})

    email = StringField(validators=[InputRequired(),Email()],render_kw={"placeholder":"email"})

    password = PasswordField(validators = {InputRequired()
       },render_kw={"placeholder":"Enter Password"})


    submit = SubmitField("SignUp")

    
def validate_email(data_field):
    if User.query.filter_by(email =data_field.data).first():
        raise ValidationError('There is an account with that email')

def validate_username(data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
        
class LoginForm(FlaskForm):
    username = StringField(validators={InputRequired(),length(min=3,
         max=10)},render_kw={"placeholder":"Enter Username"})
    
    password = PasswordField('Password',validators = [InputRequired()]
        ,render_kw={"placeholder":"Password"})

    remember = BooleanField(render_kw={'paceholder','Remember me'})

    submit = SubmitField('Login')        
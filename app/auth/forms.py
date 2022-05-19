from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, ValidationError, BooleanField)
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
    
    
class SignUpForm(FlaskForm):
    first_name = StringField("Your First Name", validators=[Required()])
    last_name = StringField("Your Last Name", validators=[Required()])    
    username = StringField("Your Username", validators=[Required()])
    email = StringField("Your Email Address", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required(), EqualTo("password_confirm", message = "Passwords must match")])
    password_confirm = PasswordField("Confirm Password", validators=[Required()])
    submit = SubmitField("Sign Up")
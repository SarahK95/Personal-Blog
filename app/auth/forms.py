from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, ValidationError, BooleanField)
from wtforms.validators import Required, Email, EqualTo
from ..models import User
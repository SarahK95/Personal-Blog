import email
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,SubmitField, SelectField)
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[InputRequired()])
    blog = TextAreaField("Input text:", validators=[InputRequired()])
    submit = SubmitField("Blog")
    
class CommentForm(FlaskForm):
    comment = TextAreaField("Blog Comment", validators=[InputRequired()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")
    
class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[InputRequired()])
    blog =  TextAreaField("Input text:", validators=[InputRequired()])
    submit = SubmitField("Update")
    
class UpdateProfile(FlaskForm):  
    first_name = StringField("First name")
    last_name = StringField("Last name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")  

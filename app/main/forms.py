import email
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,SubmitField, SelectField)
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    blog = TextAreaField("Input text:", validators=[Required()])
    submit = SubmitField("Blog")
    
class CommentForm(FlaskForm):
    comment = TextAreaField("Blog Comment", validators=[Required()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")
    
class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    blog =  TextAreaField("Input text:", validators=[Required()])
    submit = SubmitField("Update")
    
class UpdateProfile(FlaskForm):  
    first_name = StringField("First name")
    last_name = StringField("Last name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")  

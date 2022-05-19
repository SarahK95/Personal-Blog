from . import db
from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User():
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy="dynamic")
    comments = db.relationship('Blog', backref='user', lazy="dynamic")
    bio = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)  
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)   
    
    def __repr__(self):
        return f'User {self.username}'
      
    
class Blog():
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_text = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    blog_by = db.Column(db.String)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', foreign_keys = 'Comment.blog_id',backref = "blog",lazy = "dynamic")
    
  
class Comment():
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_date = db.Column(db.DateTime)
    comment_author = db.Column(db.String)
    like_count = db.Column(db.Integer, default = 0)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))  
    
class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote       
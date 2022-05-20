from . import db
from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    blog = db.relationship('Blog', backref='user', lazy="dynamic")
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
      
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_text = db.Column(db.Text)
    posted_at = db.Column(db.DateTime)
    blog_by = db.Column(db.String)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', foreign_keys = 'Comment.blog_id',backref = "blog",lazy = "dynamic")
    
  
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_date = db.Column(db.DateTime)
    comment_author = db.Column(db.String)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(cls, id):
        gone = Comment.query.filter_by(id = id).first()
        db.session.delete(gone)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id = id).all()
        return comments  
    
class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote       
        
class Subscribers(db.Model):
    __tablename__ = "subcribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)
        
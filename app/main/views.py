from crypt import methods
from flask import render_template , request, redirect, url_for
from . import main
from ..models import Blog, Comment, User, Subscribers
from flask_login import login_required, current_user
from .forms import UpdateProfile, BlogForm,  CommentForm, UpdateBlogForm
from .. import db


from ..email import welcome_message
from datetime import datetime
from app.requests import get_quote



@main.route('/')
def index():
    # blogs = Blog.get_all_posts
    quote = get_quote()   
    return render_template('index.html', quote =quote)

@main.route('/blog/<int:blog_id>', methods = ["GET", "POST"])
def blog(id):   
    blog = Blog.query.filter_by(id = id). first()
    comments = Comment.query.filter_by(blog_id = id).all()
    comment_form = CommentForm()
    comment_count = len(comments)
    
    if comment_form.validate_on_sumbit():
        comment = comment_form.comment.data
        comment_form.comment.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = "" 
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, comment_at = datetime.now(),comment_by = comment_alias,blog_id=id)    
        new_comment.save_comment()
        return redirect(url_for("main.blog", id = blog.id))       
    return render_template('blog.html', blog=blog, comments=comments, comment_form=comment_form, comment_count=comment_count)

@main.route("/blog/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    blog = Blog.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blog", id = blog.id))

@main.route("/blog/<int:id>/update", methods = ["GET", "POST"])
# @login_required
def edit_blog(id):
    blog= Blog.query.filter_by(id = id).first()
    edit_form = UpdateBlogForm()
    
    if edit_form.validate_on_submit():
        blog.blog_title = edit_form.title.data
        edit_form.title.data=""
        blog.blog_text = edit_form.blog.data
        edit_form.blog.data=""
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("main.blog", id = blog.id))
    return render_template("edit_blog.html", blog=blog, edit_form=edit_form)

@main.route("/blog/new", methods = ["GET", "POST"])
# @login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog_title = blog_form.title.data
        blog_text = blog_form.blog.data
        blog_form.title.data=""
        new_blog = Blog(blog_title = blog_title, blog_text=blog_text)
        new_blog.save_blog()       
        return redirect(url_for("main.blog", id = new_blog))
    return render_template("new_blog.html",blog_form = blog_form)

@main.route("/profile/<int:id>", methods = ["GET", "POST"])
def profile(id):
    user = User.query.filter_by(id = id).first()
    blogs = Blog.query.filter_by(user_id = id).all()
    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thank you for subscribing!", "email/welcome", new_sub.email)
        return render_template("profile/profile.html",user = user,blogs = blogs)
  
@main.route("/profile/<int:id>/<int:blog_id>/delete") 
# @login_required
def delete_blog(id, blog_id): 
    user = User.query.filter_by(id = id).first()
    blog = Blog.query.filter_by(id = blog_id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("main.profile", id = user.id))

@main.route("/profile/<int:id>/update", methods = ["GET", "POST"])
# @login_required
def update_profile(id):
    user = User.query.filter_by(id = id).first()
    form = UpdateProfile()
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.profile", id = id))
    return render_template("profile/update.html", user = user, form = form)
    
    
     
         
        

        
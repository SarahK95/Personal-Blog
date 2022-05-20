from crypt import methods
from flask import (render_template , request, redirect, url_for, abort)
from . import main
from ..models import Blog, Comment, User
from flask_login import login_required, current_user
from .forms import (UpdateProfile, BlogForm,  CommentForm, UpdateBlogForm)
from .. import db
from ..requests import get_quote
from ..email import welcome_message
from datetime import datetime



@main.route('/')
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()
    
    return render_template('index.html', blogs=blogs, quote =quote)


@main.route('/blog/<int:blog_id>', methods = ["GET", "POST"])
def blog(blog_id):
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
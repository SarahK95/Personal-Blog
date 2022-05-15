from flask import render_template
from . import main



@main.route('/')
def index():
    
    return render_template('index.html')


@main.route('post/<post_id>')
def post(post_id):
    
    return render_template('post.html', id = post_id)
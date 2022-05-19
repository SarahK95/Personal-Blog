from turtle import title
from flask import (render_template, redirect, url_for, flash, request)
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import SignUpForm, LoginForm
from .. import db

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(first_name = form.first_name.data,last_name = form.last_name.data,username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    title = "Please Sign Up"
    return render_template("auth/signup.html", signup_form = form,title = title)
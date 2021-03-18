from flask import (Flask, g, request, render_template, session, 
                   flash, redirect, url_for)

import pymysql
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user, 
                         login_required, current_user)

import forms
import models

DEBUG = True
PORT = 8000
HOST = "localhost"

app = Flask(__name__)
app.secret_key = "s23%%DFGah6.WFE@#F,@@@#123rfasgaasdcmoijessssaasaoi"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" # When users log in, redirect them to "login" view

#session------------------------------------
@login_manager.user_loader
def load_user(id):
    try:
        user = models.User.select_user(id)
        email = user["email"]
        return email
    except:
        return None

# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email

#     user.is_authenticated = request.form['password'] == users[email]['password']

#     return user

@app.before_request
def before_request():
    '''Connect to the database before each request.'''
    logged_in = session.get('logged_in')
    db = models.db


# @app.after_request
# def after_request(response):
#     '''Close the database after each request.'''
#     db = models.db
#     db.close()
#     return response


@app.route("/sign-up", methods=("GET", "POST"))
def signup():
    form = forms.RegisterForm()
    db = models.db
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if form.validate_on_submit():
        user = models.User(form.email.data, form.password.data)
        flash("Yay, you signed up!", "success") # message category
        user.insert_user()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

# session----------------------------------------------------
@app.route("/sign-in", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = models.User(form.email.data, form.password.data)
            user = user.select_user(form.email.data)
            try:
                password = user["password"]
            except TypeError:
                flash("Your email or password deosn't match!", "error")
            else:
                if check_password_hash(password, form.password.data):
                    session["logged_in"] = True
                    session["email"] = user["email"]
                    flash("You've been logged in!", "success")
                    return redirect(url_for("member"))
                else:
                    flash("Your email or password deosn't match!", "error")
    return render_template("login.html", form=form)

# @app.route("/sign-in", methods=["GET", "POST"])
# def login():
#     form = forms.LoginForm()
#     if request.method == "POST":
#         db = models.db
#         cursor = db.cursor(pymysql.cursors.DictCursor)
#         if form.validate_on_submit():
#             cursor.execute("SELECT * FROM `user` WHERE `email`= %s", (form.email.data))
#             psw = cursor.fetchone()["password"]
#             g.user = models.User(form.email.data, psw)
#             if len(psw) <= 0:
#                 flash("Your email or password deosn't match!", "error")
#             else:
#                 if check_password_hash(psw, form.password.data):
#                     g.user.is_authenticated = True
#                     login_user(g.user)
#                     flash("You've been signed in!", "success")
#                     return redirect(url_for("index"))
#                 else:
#                     flash("Your email or password deosn't match!", "error")
#     return render_template("login.html", form=form)

# session-------------------------------------------------------------
@app.route("/logout")
def logout():
    if session["logged_in"]:
        session["logged_in"] = False
        session.pop("email")
        flash("You've been logged out! Come back soon", "success")
    return redirect( url_for("index") )

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash("You've been logged out! Come back soon", "success")
#     return redirect( url_for("index") )


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member", methods=["GET", "POST"])
def member():
    form = forms.ChangePasswordForm()
    db = models.db
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if form.validate_on_submit():
        user = models.User(session["email"], form.password.data)
        user = user.select_user(session["email"])
        password = user["password"]
        if check_password_hash(password, form.oldpassword.data):
            user = models.User(session["email"], form.password.data)
            flash("Success! Remember to use new password next time.", "success") # message category
            user.update_user()
            return redirect(url_for("logout"))
        else:
            flash("Old password deosn't match!", "error")
    return render_template("member.html", form=form)


if __name__ == "__main__":
    user = models.User("test@gmail.com", "0987")
    user.update_user()
    app.run(debug=DEBUG, host=HOST, port=PORT)
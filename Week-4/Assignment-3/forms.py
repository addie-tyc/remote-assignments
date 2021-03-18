from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)
import pymysql

from models import User

def email_exists(form, field):
    db = pymysql.connect(host="localhost", user="newuser", password="assignment", database="assignment")
    cursor = db.cursor()
    result = cursor.execute("SELECT `email` FROM `user` WHERE `email`= %s", (field.data))
    if result > 0:
        raise ValidationError("User with that email already exists.")  

class RegisterForm(Form):
    email = StringField(
        "Email", # html label
        validators=[ # add some requirements for validation
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        "Password", # html label
        validators=[ # add some requirements for validation
            DataRequired(),
            Length(min=2),
            EqualTo("password2", message="Passwords must match")
        ])
    password2 = PasswordField(
        "Confirm Password", # html label
        validators=[ # add some requirements for validation
            DataRequired(),
        ])

class LoginForm(Form):
    email = StringField( "Email", validators=[ DataRequired(), Email() ] )
    password = PasswordField( "Password", validators=[ DataRequired() ] )

class ChangePasswordForm(Form):
    oldpassword = PasswordField(
        "Old Password", # html label
        validators=[ DataRequired() ])

    password = PasswordField(
        "New Password", # html label
        validators=[ # add some requirements for validation
            DataRequired(),
            Length(min=2),
            EqualTo("password2", message="Passwords must match")
        ])
    password2 = PasswordField(
        "Confirm New Password", # html label
        validators=[ # add some requirements for validation
            DataRequired(),
        ])
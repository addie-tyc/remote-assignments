import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
import pymysql

# Open database connection
db = pymysql.connect(host="localhost", user="newuser", password="assignment", database="assignment")

class User(UserMixin):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.password_hash = generate_password_hash(password)
    
    def get_id(self):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT `email` FROM user WHERE email = %s', (self.email))
        try:
            email = cursor.fetchone()[0]["email"]
            if email:
                return email
        except:
            return None
    
    def select_user(self, email):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email))
        try:
            user = cursor.fetchone() # a dict
            if user:
                return user
        except:
            return None

    def insert_user(self):
        cursor = db.cursor()
        cursor.execute('INSERT INTO user(email, password) VALUES(%s,%s)',
                       (self.email, self.password_hash))
        db.commit()

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def update_user(self):
        cursor = db.cursor()
        cursor.execute('UPDATE user SET `password` = %s WHERE `email` = %s',
                       (self.password_hash, self.email))
        db.commit()


def get_password_hash(email):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT `password` FROM user WHERE email = %s', (email))
        psw = cursor.fetchone()["password"]
        if psw:
            return psw
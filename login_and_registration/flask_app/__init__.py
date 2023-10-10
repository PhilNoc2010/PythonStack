from flask import Flask
app = Flask(__name__)
app.secret_key = "Your Princess is in another castle"
import re


DATABASE = "logins_db"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
CHAR_REGEX = re.compile(r'^[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{8,}$')
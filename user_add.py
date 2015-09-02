#!flask/bin/python
from app import db
from app.models import User
from pbkdf2 import crypt

username = raw_input('Username: ')
password = raw_input('Password: ')
u = User(username=username, pwhash=crypt(password), permissions=4)
db.session.add(u)
db.session.commit()

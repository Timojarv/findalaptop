from .models import User
from pbkdf2 import crypt

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None or user.pwhash != crypt(password, user.pwhash):
        return False
    return user

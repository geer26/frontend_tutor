import json
from app import db
from app.models import User, Entry

def adduser(data):
    username = data['username']
    try:
        user = User()
        user.username = username
        return True
    except(Exception):
        return False
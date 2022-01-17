import json
from app import db
from app.models import User, Entry

def adduser(data):
    username = data['username']
    try:
        user = User()
        user.username = username
        db.session.add(user)
        db.session.commit()
        return True
    except(Exception):
        return False


def deluser(data):
    userid = data['userid']
    try:
        user = User.query.get(int(userid))
        # delete all corresponding entries
        for entry in Entry.query.filter_by(author=user.id).all():
            db.session.delete(entry)
        db.session.delete(user)
        db.session.commit()
        return True
    except(Exception):
        return False


def addentry(data):
    pass
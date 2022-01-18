import json
from datetime import datetime
from app import db
from app.models import User, Entry

def adduser(data):
    try:
        username = data['username']
        user = User()
        user.username = username
        db.session.add(user)
        db.session.commit()
        return True
    except(Exception):
        return False


def deluser(data):
    try:
        userid = data['userid']
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
    try:
        entry = Entry()
        entry.title = str(data['title'])
        entry.body = str(data['body'])
        entry.author = int(data['author'])
        db.session.add(entry)
        db.session.commit()
        return True
    except(Exception):
        return False


def delentry(data):
    try:
        entryid = data['entryid']
        entry = Entry.query.get(int(entryid))
        db.session.delete(entry)
        db.session.commit()
        return True
    except(Exception):
        return False


def modentry(data):
    try:
        entryid = data['entryid']
        entry = Entry.query.get(int(entryid))
        entry.title = str(data['title'])
        entry.body = str(data['body'])
        return True
    except(Exception):
        return False


def getdata():
    try:
        data = []
        for user in User.query.all():
            u = {}
            u['userid'] = user.id
            u['username'] = user.username
            u['entries'] = []
            for entry in Entry.query.filter_by(author=user.id).all():
                print(f'ENTRY: {entry.get_self_json()}')
                e = {}
                e['id'] = entry.id
                e['title'] = entry.title
                e['body'] = entry.body
                e['author'] = entry.author
                e['created_at'] = entry.created_at
                u['entries'].append(e)
            data.append(u)
        return data
    except(Exception):
        return False
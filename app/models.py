import json, uuid
from app import db
import bcrypt
from datetime import datetime
#from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)

    def __repr__(self):
        return f'Username: {self.username}, ID: {self.id}'

    def get_self_json(self):
        return {
            'id': self.id,
            'username': self.username
        }


class Entry(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    title = db.Column(db.String(64), default='No title')
    body = db.Column(db.String(4096), default='No body')
    created_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Username: {self.username}, ID: {self.id}'

    def get_self_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'author': self.author
        }
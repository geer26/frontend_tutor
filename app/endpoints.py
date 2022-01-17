import json
import os
from datetime import datetime
from flask_restful import Resource
#from flask_login import current_user, login_user, logout_user
from flask import request, render_template, send_from_directory, session, Response, redirect
from app import api, db

from app.workers import adduser, deluser

from app.models import User, Entry


class AddUser(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if adduser(json_data):
            return {'status': 0, 'message': 'User added!'}, 200
        return {'status': 1, 'message': 'Error occured!'}, 500


class DelUser(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if deluser(json_data):
            return {'status': 0, 'message': 'User deleted!'}, 200
        return {'status': 1, 'message': 'Error occured!'}, 500





api.add_resource(AddUser, '/API/adduser')
api.add_resource(DelUser, '/API/deluser')
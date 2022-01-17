import json
import os
from datetime import datetime
from flask_restful import Resource
#from flask_login import current_user, login_user, logout_user
from flask import request, render_template, send_from_directory, session, Response, redirect
from app import api, db

from app.workers import adduser

'''
from app.workers import pw_complexity, addsu, adduser, get_all_data, deluser, add_exercise,\
    del_exercise, get_user_exercises, check_exercise_belonging, mod_exercise, add_workout, \
    get_user_workouts, del_workout, edit_workout, add_event, get_user_events, del_event, \
    swap_event_enable, get_single_event, mod_event, get_settingsmode_data, get_competitorsdata, \
    addcompetitor, update_sequence, get_competitordata, fetch_userevents, fetch_event
'''

from app.models import User, Entry


class AddUser(Resource):
    def post(self):

        json_data = request.get_json(force=True)
        if adduser(json_data):
            return {'status': 0, 'message': 'User added!'}, 200
        return {'status': 1, 'message': 'Error occured!'}, 500




api.add_resource(AddUser, '/API/adduser')
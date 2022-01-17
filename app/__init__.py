from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login import LoginManager
from config import Config
from flask_restful import Api
from flask_cors import CORS
#from flask_socketio import SocketIO
#from roomhandler import Roomhandler


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db, render_as_batch=True)

#login = LoginManager(app)

api = Api(app)

#socket = SocketIO(app)
#socket.init_app(app, cors_allowed_origins="*")

#handler=Roomhandler()

#from app import routes, models, workers, endpoints
from app import models, endpoints
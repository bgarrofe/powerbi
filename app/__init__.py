import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
from flask import Flask
from config import Config
import requests
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # enable non-HTTPS for testing

app = Flask(__name__)
#api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
SESSION = requests.Session()

from app import routes

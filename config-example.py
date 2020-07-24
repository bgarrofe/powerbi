import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = 'you-secret-key'

    CLIENT_ID = 'your-client-id'
    CLIENT_SECRET = 'your-client-secret'

    REDIRECT_URI = 'http://127.0.0.1:5000/login/authorized'

    # AUTHORITY_URL ending determines type of account that can be authenticated:
    # /organizations = organizational accounts only
    # /consumers = MSAs only (Microsoft Accounts - Live.com, Hotmail.com, etc.)
    # /common = allow both types of accounts
    AUTHORITY_URL = 'https://login.microsoftonline.com/common'

    AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
    TOKEN_ENDPOINT = '/oauth2/v2.0/token'

    RESOURCE = 'https://analysis.windows.net/powerbi/api'
    API_VERSION = 'v1.0'
    SCOPES = ['openid', 'profile'] # Add other scopes/permissions as needed.

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

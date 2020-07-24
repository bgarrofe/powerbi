from flask import Flask, render_template, session, request, redirect, url_for
from flask_restplus import Resource
#from app import app, api, SESSION
from app import app, SESSION
import urllib.parse
import uuid
import adal

@app.route('/')
def homepage():
    """Render the home page."""
    return render_template('index.html', sample='ADAL')

@app.route('/login')
def login():
    """Prompt user to authenticate."""
    SESSION.auth_state = str(uuid.uuid4())

    params = urllib.parse.urlencode({'response_type': 'code',
                                     'client_id': app.config['CLIENT_ID'],
                                     'redirect_uri': app.config['REDIRECT_URI'],
                                     'state': SESSION.auth_state,
                                     'resource': app.config['RESOURCE'],
                                     'prompt': 'select_account',
                                     'scope': 'openid%20offline_access'})

    return redirect(app.config['AUTHORITY_URL'] + '/oauth2/authorize?' + params)
    #return redirect(app.config['AUTHORITY_URL'] + app.config['AUTH_ENDPOINT'] + '?' + params)

@app.route('/login/authorized')
def authorized():
    """Handler for the application's Redirect Uri."""
    code = request.args['code']
    auth_state = request.args['state']
    if auth_state != SESSION.auth_state:
        raise Exception('state returned to redirect URL does not match!')
    auth_context = adal.AuthenticationContext(app.config['AUTHORITY_URL'], api_version=None)
    token_response = auth_context.acquire_token_with_authorization_code(
        code, app.config['REDIRECT_URI'], app.config['RESOURCE'], app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])
    
    session['accessToken'] = token_response['accessToken']
    session['refreshToken'] = token_response['refreshToken']

    headers = {
        'Authorization': f"Bearer {token_response['accessToken']}",
        'User-Agent': 'adal-sample',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'SdkVersion': 'sample-python-adal',
        'return-client-request-id': 'true'
    }

    SESSION.headers.update(headers)
    return redirect('/home')

@app.route('/home')
def home():
    endpoint = 'https://api.powerbi.com/v1.0/myorg/datasets'
    #endpoint = 'https://wabi-south-central-us-redirect.analysis.windows.net/export/xlsx'
    token = session['accessToken']
    refresh = session['refreshToken']
    
    return render_template('home.html', sample='ADAL', token=token, refresh=refresh)

# @api.route('/api/hello/')
# class HelloWorld(Resource):
#     def get(self):
#         return "Hello World"

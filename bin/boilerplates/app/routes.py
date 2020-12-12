from flask import render_template

from app import app
from app.blueprints.user_management.views import session



@app.before_request
@session.verify_role
def before_request():
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return 'login_screen'

@app.route('/logout')
def logout():
    return 'logout action'
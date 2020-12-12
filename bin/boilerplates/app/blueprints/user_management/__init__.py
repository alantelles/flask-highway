from flask import Blueprint, render_template, request
import os

import app.blueprints.user_management.views.users as users_views
import app.blueprints.user_management.views.roles as roles_views




user_management = Blueprint('user_management', __name__, template_folder='templates')

@user_management.route('')
def index():
    controllers_list = os.listdir(os.path.join(os.getcwd(), 'app', 'blueprints', 'user_management', 'views'))
    filtered = [filt for filt in controllers_list if not filt.startswith('__')]
    return render_template("user_management/index.html", views=filtered)

@user_management.route('/users/')
def users_index():
    return users_views.index()

@user_management.route('/users/<id>/')
def users_show(id):
    return users_views.show(id)

@user_management.route('/users/new/', methods=['GET'])
def users_new():
    return users_views.new()

@user_management.route('/users/new/', methods=['POST'])
def users_create():
    return users_views.create()

@user_management.route('/roles/new/', methods=['GET'])
def roles_new():
    return roles_views.new()

@user_management.route('/roles/new/', methods=['POST'])
def roles_create():
    return roles_views.create()

@user_management.route('/roles/', methods=['GET'])
def roles_index():
    return roles_views.index()

@user_management.route('/roles/<id>/', methods=['GET'])
def roles_show(id):
    return roles_views.show(id)

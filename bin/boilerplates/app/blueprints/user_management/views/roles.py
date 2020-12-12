from flask import render_template, redirect, request
from app import db
from app.blueprints.user_management.models.role import Role

def index():
    roles = Role.query.all()
    return render_template('user_management/roles/index.html', roles=roles)

def create():
    name = request.form['name']
    role = Role(name=name)
    db.session.add(role)
    db.session.commit()
    return 'saved'

def new():
    return render_template('user_management/roles/new.html')

def show(id):
    role = Role.query.filter_by(id=id).first()
    return render_template('user_management/roles/show.html', role=role)
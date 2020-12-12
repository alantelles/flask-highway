from flask import render_template, request, redirect, url_for
from app.blueprints.user_management.models.user import User
from app.blueprints.user_management.models.role import Role
from app import db

def index():
    users = User.query.all()
    return render_template('user_management/users/index.html', users=users)

def show(id):
    user = User.query.filter_by(id=id).first()
    return render_template('user_management/users/show.html', user=user)

def new():
    roles = Role.query.all()
    return render_template('user_management/users/new.html', roles=roles)

def create():
    post_data = request.form
    roles_ids = [int(id) for id in request.form.getlist('roles')]
    roles = db.session.query(Role).filter(Role.id.in_(roles_ids)).all()
    
    user = User(
        name=post_data['name'],
        username=post_data['username'],
        password_hash=User.set_password(post_data['password'])
    )
    for r in roles:
        user.roles.append(r)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('user_management.users_show', id=user.id))
    
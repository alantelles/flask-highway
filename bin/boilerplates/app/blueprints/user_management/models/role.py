from app import db
from app.blueprints.user_management.models.user_roles import user_roles

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), default='normal')
    users = db.relationship('Role', secondary=user_roles, backref=db.backref('User'))
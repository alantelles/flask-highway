from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

from app import config

db = SQLAlchemy(app)


from app import routes

from app.blueprints.user_management import user_management
app.register_blueprint(user_management, url_prefix='/user_management')

try:
    db.create_all()
    db.session.commit()
except Exception as e:
    print(f"Tables not created because: {e}")
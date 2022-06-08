from flask import Flask
from routes.tiktok_user import tiktok
import os
#from config import DATABASE_CONNECTION_URI
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import true
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
  
app.config ["SQLALCHEMY_DATABASE_URI"]='sqlite:///' + os.path.join(BASE_DIR,'database.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
SQLAlchemy(app)
app.register_blueprint(tiktok)


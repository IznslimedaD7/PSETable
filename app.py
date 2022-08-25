from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
ckeditor = CKEditor(app)
login_manager = LoginManager(app)
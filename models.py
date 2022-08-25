from app import db
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Elements (db.Model):
    __tablename__ = 'element'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Elements %r>' % self.id

class Users (db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def ___repr__(self):
        return  '<Users %r>' % self.id

    def check_password(self, password):
        return check_password_hash(generate_password_hash(password), password)
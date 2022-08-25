from wtforms import StringField, SubmitField, TextAreaField, BooleanField, PasswordField
from flask_wtf import  FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import Email, Length
import email_validator


class MyForm(FlaskForm):
    email = EmailField(label='E-mail', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='Go')

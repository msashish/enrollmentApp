# This is a web form (Flask WTF) for those html structures where we have data input and user interaction
# Hidden fields are not defined
# While rendering html pages, we pass the forms as below examples:
#          render_template("login.html", title='Login', form=login_form, login=True)
#          render_template("register.html", title="Register", form=register_form, register=True)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from application.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=16)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=16)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=16),
                                                                   EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField('Register Now')

    def validate_email(self, email):
        if User.objects(email=email.data).first():
            raise ValidationError("Email entered has already been registered !! ")

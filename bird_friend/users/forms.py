from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired, Email, EqualTo, ValidationError, Length)
from bird_friend.models import User
from flask_login import current_user

#App forms from student project - 
#https://github.com/cjcon90/hot-dogz/blob/main/hot_dogz/users/forms.py

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(
                               message="Please enter a username")])
    password = PasswordField('Password',
                             validators=[DataRequired(
                                 message="Please enter a password")])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(message="Please enter a username"),
                               Length(min=2, max=12,
                                      message="Please enter a username "
                                              "between 2 and 12 characters "
                                              "long")])
    email = StringField('Email',
                        validators=[
                            DataRequired(message="Please enter an email"),
                            Email(
                                message="Please enter a valid email address"),
                            Length(max=100, message="Email is too long "
                                                    "(100 character max)")])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(
                                     message="Please enter a password")])
    password2 = PasswordField(
        'Repeat Password',
        validators=[
            DataRequired(message="Please double check password"),
            EqualTo('password', message="Passwords don't match! "
                                        "Please try again")])
    submit = SubmitField('Register')

    # Function to check that username isn't already registered on site
    def validate_username(self, username):
        existing = User.objects(username=username.data).first()
        if existing is not None:
            raise ValidationError('Please use a different username.')

    # Function to check that email isn't already registered on site
    def validate_email(self, email):
        existing = User.objects(email=email.data).first()
        if existing is not None:
            raise ValidationError('Please use a different email.')


class RequestPasswordForm(FlaskForm):
    email = StringField(
        'Your Email Address', validators=[
            DataRequired(message="Please enter your email address"),
            Email(message="Please enter a valid email address")])
    submit = SubmitField('Submit')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired(
                                 message="Please enter your new password")])
    password2 = PasswordField(
        'Repeat Password',
        validators=[
            DataRequired(message="Please double check password"),
            EqualTo('password',
                    message="The passwords don't match! Please try again")])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(message="Please enter a username"),
                               Length(min=2, max=12,
                                      message="Please enter a username "
                                              "between "
                                              "2 and 12 characters long")])
    email = StringField(
        'Email', validators=[
            DataRequired(message="Please enter an email"),
            Email(message="Please enter a valid email address"),
            Length(max=100, message="Email is too long "
                                    "(100 character max)")])
    submit = SubmitField('Submit')

    # Function to check that username (if new) isn't already registered on site
    def validate_username(self, username):
        if username.data != current_user.username:
            existing = User.objects(username=username.data).first()
            if existing is not None:
                raise ValidationError('Please use a different username.')

    # Function to check that email (if new) isn't already registered on site
    def validate_email(self, email):
        if email.data != current_user.email:
            existing = User.objects(email=email.data).first()
            if existing is not None:
                raise ValidationError('Please use a different email.')


class DeleteAccountForm(FlaskForm):
    password = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Delete Account')

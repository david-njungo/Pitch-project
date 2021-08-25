from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Email, Length
from ..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField


class RegistrationForm(FlaskForm):
    first_name = StringField('first name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = StringField('last name', validators=[InputRequired(), Length(min=4, max=15)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Register')

    def validate_email(self,data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
    submit = SubmitField('Log in')

class PitchForm(FlaskForm):
    author = IntegerField('author', validators=[InputRequired()])
    category = IntegerField('category', validators=[InputRequired()])
    description = StringField('description', widget=TextArea(), validators=[InputRequired(), Length(min=10, max=255)])
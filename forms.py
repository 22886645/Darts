from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField, SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo
# from flask_wtf import FlaskForm

# from wtform import Form


class RegisterationForm(FlaskForm):
username = StringField('username:', validators=[DataRequired(),Length(min=1,max=25)])
email = StringField('email:',validators=[DataRequired()])
password = PasswordField('password:' , validators=[DataRequired()])
confirm_passwod = PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
submit = SubmitField('go')

class LoginForm(FlaskForm):
email = StringField('email',validators=[DataRequired()])
password = PasswordField('password' , validators=[DataRequired()])
remember = BooleanField('remember me')
submit = SubmitField('go')

class updateprofileForm(FlaskForm):
username = StringField('username', validators=[DataRequired(),Length(min=1,max=25)])
email = StringField('email',validators=[DataRequired()])
password = StringField('password',validators=[DataRequired()])

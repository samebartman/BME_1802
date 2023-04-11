from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, DateField, TextAreaField
from wtforms.fields.html5 import EmailField, IntegerField, DateField
from wtforms.validators import ValidationError, DataRequired, Length, Optional, InputRequired, Email, EqualTo

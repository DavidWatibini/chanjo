from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class BookForm(FlaskForm):

    child_name = StringField('Child Name',validators=[Required()])
    child_age = StringField('Child Age',validators = [Required()])
    submit = SubmitField('submit')

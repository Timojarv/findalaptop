from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SelectField
from flask.ext.wtf.html5 import RangeInput
from wtforms.validators import DataRequired
from .models import User

class ImportanceForm(Form):
    performance = IntegerField('Performance', widget=RangeInput())
    screen = IntegerField('Screen quality', widget=RangeInput())
    sound = IntegerField('Sound quality', widget=RangeInput())
    mobility = IntegerField('Mobility', widget=RangeInput())
    battery = IntegerField('Battery', widget=RangeInput())

class LoginForm(Form):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=True)

    def validate(self):
        if not Form.validate(self):
            return False

        if ' ' in self.user.data:
            self.user.errors.append("Usernames cannot contain spaces!")
            return False

        return True

class UserEditForm(Form):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    permissions = SelectField('permissions', choices=[('1', 'Standard user'), ('2', 'Moderator'), ('3', 'Admin'), ('4', 'Lead Admin')], validators=[DataRequired()])

    def __init__(self, original_username="", *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not Form.validate(self):
            return False

        if self.user.data == self.original_username:
            return True

        user = User.query.filter_by(username=self.user.data).first()
        if user != None:
            self.user.errors.append('Sorry, but that username is already in use.')
            return False

        if ' ' in self.user.data:
            self.user.errors.append("Usernames cannot contain spaces!")
            return False

        return True

class AddForm(Form):
    make = StringField('Make') #Laptop brand
    model = StringField('Model') #Model of the laptop
    specs = StringField('Specs') #Json array of specs in string form
    performance = IntegerField('Performance', widget=RangeInput()) #All the scores are below in integer form
    screen = IntegerField('Screen', widget=RangeInput())
    sound = IntegerField('Sound', widget=RangeInput())
    mobility = IntegerField('Mobility', widget=RangeInput())
    battery = IntegerField('Battery', widget=RangeInput())

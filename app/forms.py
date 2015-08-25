from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField
from flask.ext.wtf.html5 import RangeInput
from wtforms.validators import DataRequired


class ImportanceForm(Form):
    performance = IntegerField('Performance', widget=RangeInput())
    screen = IntegerField('Screen quality', widget=RangeInput())
    sound = IntegerField('Sound quality', widget=RangeInput())
    mobility = IntegerField('Mobility', widget=RangeInput())
    battery = IntegerField('Battery', widget=RangeInput())

class LoginForm(Form):
    user = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])

class AddForm(Form):
    make = StringField('Make') #Laptop brand
    model = StringField('Model') #Model of the laptop
    specs = StringField('Specs') #Json array of specs in string form
    performance = IntegerField('Performance', widget=RangeInput()) #All the scores are below in integer form
    screen = IntegerField('Screen', widget=RangeInput())
    sound = IntegerField('Sound', widget=RangeInput())
    mobility = IntegerField('Mobility', widget=RangeInput())
    battery = IntegerField('Battery', widget=RangeInput())

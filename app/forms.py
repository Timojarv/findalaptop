from flask.ext.wtf import Form
from wtforms import StringField

class TestForm(Form):
    test = StringField('testing')

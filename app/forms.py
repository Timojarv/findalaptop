from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask.ext.wtf.html5 import RangeInput


class TestForm(Form):
    performance = IntegerField('Performance', widget=RangeInput())
    screen = IntegerField('Screen quality', widget=RangeInput())
    sound = IntegerField('Sound quality', widget=RangeInput())
    mobility = IntegerField('Mobility', widget=RangeInput())
    battery = IntegerField('Battery', widget=RangeInput())

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
    password = PasswordField('Password')
    permissions = SelectField('permissions', choices=[('1', 'Standard user'), ('2', 'Moderator'), ('3', 'Admin'), ('4', 'Project Lead')], validators=[DataRequired()])
    remove = BooleanField('remove', default=False)

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

class LaptopEditForm(Form):
    brand = StringField('Brand') #Laptop brand
    model = StringField('Model') #Model of the laptop
    cpuBrand = StringField('Cpu Brand')
    cpuModel = StringField('Cpu Model')
    ram = IntegerField('Ram (GB)')
    gpuBrand = StringField('Gpu Brand')
    gpuModel = StringField('Gpu Model')
    ssd = IntegerField('SSD Size')
    hdd = IntegerField('HDD Size')
    odd = StringField('Optical Drive')
    screenW = IntegerField('Screen Width')
    screenH = IntegerField('Screen height')
    touch = BooleanField('Touch screen')
    batteryWh = IntegerField('Battery Wh')
    batteryTime = IntegerField('Battery Time (h)')
    width = IntegerField('Width (mm)')
    length = IntegerField('Length (mm)')
    thickness = IntegerField('Thickness (mm)')
    weight = IntegerField('Weight (g)')
    size = IntegerField('Screen size')
    price = IntegerField('Price') #Laptop price

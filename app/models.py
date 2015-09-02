from app import db

class Laptop(db.Model):
    '''
    Laptop specs array specification:
    specs = [0cpuBrand, 1cpuModel, 2ramGB, 3gpuBrand, 4gpuModel, 5ssdGB, 6hddGB, 7odd, 8screenW, 9screenH, 10touch, 11batteryWh, 12batteryTime, 13width, 14length, 15thickness, 16weight]
    '''
    id = db.Column(db.Integer, primary_key=True) #Unique id for primary key purposes only
    brand = db.Column(db.String(12), index=True) #Laptop brand
    model = db.Column(db.String(24), index=True) #Model of the laptop
    specs = db.Column(db.String(512)) #Json array of specs in string form
    price = db.Column(db.Integer, index=True)#price of the laptop
    size = db.Column(db.Integer, index=True)#screen diagonal

    def __repr__(self):
        return '<%s %s>' % (self.make, self.model)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    pwhash = db.Column(db.String(64))
    permissions = db.Column(db.Integer, index=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)

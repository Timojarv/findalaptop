from app import db

class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique id for primary key purposes only
    make = db.Column(db.String(12), index=True) #Laptop brand
    model = db.Column(db.String(24), index=True) #Model of the laptop
    specs = db.Column(db.String(128)) #Json array of specs in string form
    performance = db.Column(db.Integer, index=True) #All the scores are below in integer form
    screen = db.Column(db.Integer, index=True)
    sound = db.Column(db.Integer, index=True)
    mobility = db.Column(db.Integer, index=True)
    battery = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<%s %s>' % (self.make, self.model)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    pwhash = db.Column(db.String(64))

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

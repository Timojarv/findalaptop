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

from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    firstname = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    nickname = db.Column(db.String(1000))
    birthdate = db.Column(db.Date())
    telephone = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    responsavel = db.Column(db.Boolean())
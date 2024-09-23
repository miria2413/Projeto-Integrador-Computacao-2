from flask_login import UserMixin
from . import db

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resp_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    firstname = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    nickname = db.Column(db.String(1000))
    birthdate = db.Column(db.Date())
    telephone = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    responsavel = db.relationship('Usuario', remote_side=[id], )
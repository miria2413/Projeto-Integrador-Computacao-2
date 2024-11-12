from flask_login import UserMixin
from . import db


UsuarioAtividade = db.Table(
    'usuario_atividade',
    db.metadata,
    db.Column('usuario_id', db.ForeignKey('usuario.id')),
    db.Column('atividade_id', db.ForeignKey('atividade.id')),
    db.Column('data', db.Date),
    db.Column('concluido', db.Boolean))
    

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
    responsavel = db.relationship('Usuario', remote_side=[id])
    atividades = db.relationship('Atividade', secondary=UsuarioAtividade, backref='Atividade')

class CategoriaAtividade(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(1000))

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categ_id = db.Column(db.Integer, db.ForeignKey('categoria_atividade.id'))
    nome = db.Column(db.String(1000))
    descricao = db.Column(db.String(1000))
    idade_minima = db.Column(db.Integer)
    idade_maxima = db.Column(db.Integer)
    pontos = db.Column(db.Integer)
    usuarios = db.relationship('Usuario', secondary=UsuarioAtividade, backref='Usuario')
    categoria = db.relationship('CategoriaAtividade', backref='atividade')

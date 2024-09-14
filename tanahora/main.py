from flask import Blueprint, render_template, redirect, url_for, request

from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

# Rota para a página de inical
@main.route('/')
def pagina_login():
    return render_template('index.html')

@main.route('/home')
def home_inicial():
    return render_template('index.html')

@main.route('/perfil')
def perfil():
    return render_template('perfil.html')

# Rota para a página sobre
@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página sobre responsável
@main.route('/sobre1')
def sobre1():
    return render_template('sobre1.html')

# Rota para a página sobre dependente
@main.route('/sobre2')
def sobre2():
    return render_template('sobre2.html')        



# Rota para cadastro dependente
@main.route('/cadastro2')
def cadastro2():
    return render_template('cadastro2.html')

# Rota para a página home responsável
@main.route('/home_resp')
def home_resp():
    return render_template('home1.html')

# Rota para a página atividade responsável
@main.route('/ativ1')
def ativ1():
    return render_template('ativ1.html')    

# Rota para a página atividade dependente
@main.route('/ativ2')
def ativ2():
    return render_template('ativ2.html') 


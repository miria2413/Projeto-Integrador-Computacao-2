from .models import Usuario
from flask import Blueprint, render_template, redirect, url_for, request

from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

# Rota para a página de inical
@main.route('/')
@main.route('/index')
def pagina_inicial():
    return render_template('index.html')


# Rota para a página sobre
@main.route('/sobre')
def sobre():
    return render_template('sobre.html')


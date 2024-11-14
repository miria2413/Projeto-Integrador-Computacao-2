from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario, Atividade
from . import db
from functools import wraps

auth = Blueprint('auth', __name__)


def requer_responsavel(func):
    """
    Permissão para as páginas do responsável
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.resp_id is not None:
            flash("Apenas responáveis podem acessar essa página.", "warning")
            return redirect(url_for("auth.home"))
        return func(*args, **kwargs)
    return decorated_view

# Rota para a página de cadastro responsável
@auth.route('/cadastro')
def cadastro():
    return render_template('cadastro-responsavel.html')

@auth.route('/cadastro', methods=['POST'])
def cadastro_post():

    email = request.form.get('email')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    nickname = request.form.get('nickname')
    birthdate = request.form.get('birthdate')
    telephone = request.form.get('telephone')
    gender = request.form.get('gender')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first() # se email já existir, vai retornar o usuário

    if user: # se o usuário existir, redireciona para o login
        return redirect(url_for('auth.login'))

    # Cria um novo usuário responsável.
    new_user = Usuario(email = email,
                       firstname = firstname, 
                       lastname = lastname, 
                       nickname = nickname, 
                       birthdate = birthdate, 
                       telephone = telephone, 
                       gender = gender,
                       password=generate_password_hash(password))

    # Persiste no banco
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('lembrar') else False

    user = Usuario.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    if user.resp_id is None:
        return redirect(url_for('auth.home_responsavel'))
    return redirect(url_for('auth.home_dependente'))

@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', usuario=current_user)

@auth.route('/home')
@login_required
def home():
    if current_user.resp_id is None:
        return redirect(url_for('auth.home_responsavel'))
    return redirect(url_for('auth.home_dependente'))

@auth.route('/responsavel')
@requer_responsavel
def home_responsavel():
    return render_template('home-responsavel.html', usuario=current_user)

@auth.route('/responsavel/atividade')
@login_required
@requer_responsavel
def cadastro_atividade():
    lista_atividades = Atividade.query.all()
    return render_template('atividades.html', lista_atividades=lista_atividades)

@auth.route('/responsavel/dependente/adicionar')
@login_required
@requer_responsavel
def adicionar_dependente(responsavel = current_user):
    return render_template('adicionar-dependente.html')

@auth.route('/responsavel/dependente/adicionar', methods=['POST'])
@login_required
@requer_responsavel
def cadastro_dependente_post():

    email = request.form.get('email')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    nickname = request.form.get('nickname')
    birthdate = request.form.get('birthdate')
    telephone = request.form.get('telephone')
    gender = request.form.get('gender')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first() # se email já existir, vai retornar o usuário

    if user: # se o usuário existir, redireciona para o login
        return redirect(url_for('auth.login'))

    # Cria um novo usuário responsável.
    new_user = Usuario(email = email,
                       firstname = firstname, 
                       lastname = lastname, 
                       nickname = nickname, 
                       birthdate = birthdate, 
                       telephone = telephone, 
                       gender = gender,
                       password=generate_password_hash(password),
                       resp_id = current_user.id)

    # Persiste no banco
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.home_responsavel'))


@auth.route('/dependente')
@login_required
def home_dependente():
    return render_template('home-dependente.html', usuario=current_user)

@auth.route('/calendario')
@login_required
def calendario():
    return render_template('calendario.html', usuario=current_user)
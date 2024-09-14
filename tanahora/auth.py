from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario
from . import db

auth = Blueprint('auth', __name__)

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
    return redirect(url_for('main.perfil'))


# Rota para a página de cadastro responsável
@auth.route('/cadastro')
def cadastro():
    return render_template('cadastrop.html')

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
    responsavel = True

    user = Usuario.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.login'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Usuario(email = email,
                       firstname = firstname, 
                       lastname = lastname, 
                       nickname = nickname, 
                       birthdate = birthdate, 
                       telephone = telephone, 
                       gender = gender, 
                       responsavel = responsavel, 
                       password=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


# Rota para a página home dependente
@auth.route('/home_dependente')
def home_dependente():
    return render_template('home2.html')


@auth.route('/logout')
def logout():
    return 'Logout'
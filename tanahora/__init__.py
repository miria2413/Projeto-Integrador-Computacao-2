from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():

    # A chave secreta é usada para assinar os cookies de sessão, garantindo que não possam ser falsificados ou manipulados por terceiros
    app = Flask(__name__)

    #
    app.secret_key = 'teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://tanahora:tanahora@localhost/tanahora'
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


# Cria tabelas a partir do models.py no Banco de dados 
# with create_app().app_context():
#     db.create_all()
# AS instalações são realizadas no prompt de comando 
# pip install flask
# pip install mysql-connector-python


from flask import Flask, request, render_template, redirect, jsonify, session
import mysql.connector

# A chave secreta é usada para assinar os cookies de sessão, garantindo que não possam ser falsificados ou manipulados por terceiros
app = Flask(__name__)

#
app.secret_key = 'teste'

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="N&na9118",
    database="tanahora"
)
cursor = conn.cursor()

# Rota para a página de inical
@app.route('/')
def pagina_login():
    return render_template('home.html')

@app.route('/home')
def home_inicial():
    return render_template('home.html')

# Rota para a página de login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para a página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página sobre responsável
@app.route('/sobre1')
def sobre1():
    return render_template('sobre1.html')

# Rota para a página sobre dependente
@app.route('/sobre2')
def sobre2():
    return render_template('sobre2.html')        

# Rota para a página de cadastro responsável
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro1.html')

# Rota para cadastro dependente
@app.route('/cadastro2')
def cadastro2():
    return render_template('cadastro2.html')

# Rota para a página home responsável
@app.route('/home_resp')
def home_resp():
    return render_template('home1.html')

# Rota para a página home dependente
@app.route('/home_dependente')
def home_dependente():
    return render_template('home2.html')

# Rota para a página atividade responsável
@app.route('/ativ1')
def ativ1():
    return render_template('ativ1.html')    

# Rota para a página atividade dependente
@app.route('/ativ2')
def ativ2():
    return render_template('ativ2.html') 

@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    data = request.json
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    nick = data.get('nick')
    datanascimento = data.get('datanascimento')
    dependentes = data.get('dependentes')
    telefone = data.get('telefone')
    email = data.get('email')
    senha = data.get('senha')
    genero = data.get('genero')
    
  
    dados = (nome, sobrenome, nick, datanascimento, dependentes, telefone, email, senha, genero)
    print(dados)

    # Consulta SQL para inserir os dados no banco de dados
    cursor.execute("INSERT INTO responsavel (nome, sobrenome, nick, datanascimento, dependentes, telefone, email, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, sobrenome, nick, datanascimento, dependentes, telefone, email, senha, genero))
       
    conn.commit()
    
    return render_template('login.html')

# Rota para verificar as credenciais de login e redirecionar para home de acesso
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    data = request.json
    login = data['login']
    senha = data['senha']
    

    # Consulta SQL para verificar o login no banco de dados
    cursor.execute("SELECT * FROM responsavel WHERE email = %s AND senha = %s", (login, senha))
    responsavel = cursor.fetchone()
    print(responsavel)
   
    cursor.execute("SELECT * FROM dependente WHERE emaild = %s AND senhad = %s", (login, senha))
    dependente = cursor.fetchone()
    print(dependente)
       
    if responsavel:
        resp_id = responsavel[0]
        session['resp_id'] = resp_id 
        return jsonify({'redirect_url': '/home_resp'})
    elif dependente:
        return jsonify({'redirect_url': '/home_dependente'})
    else:
        return jsonify({'mensagem': 'Login inválido'}), 401



@app.route('/dados-dependente', methods=['POST'])
def dados_dependente():
    data = request.json
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    nick = data.get('nick')
    datanascimento = data.get('datanascimento')
    telefone = data.get('telefone')
    email = data.get('email')
    senha = data.get('senha')
    genero = data.get('genero')
    
    id_resp = session['resp_id']

    dados = (nome, sobrenome, nick, datanascimento, telefone, email, senha, genero)
    print(dados)

    cursor.execute("INSERT INTO dependente (nomed, sobrenomed, nickd, datanascimentod, telefoned, emaild, senhad, generod, id_resp_dep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, sobrenome, nick, datanascimento, telefone, email, senha, genero, id_resp))
    conn.commit()
    
    return render_template('home1.html')


    # Redirecionar para a próxima página
    return redirect(f'/login')

  
if __name__ == '__main__':
    app.run(debug=True)    

<h1 align="center"> Projeto Integrador II</h1>

<p align="center">
Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente, incluir análise de dados.
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>


## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- HTML e CSS
- Python (Flask)
- Git e Github

## 💻 Projeto

Um site voltado para a Interação Familiar com dicas de atividades e brincadeira para promover momentos de diversão em familia , usando gamificação.

## Criação do ambiente e Execução

### Instalando

1. Criando o ambiente virtual Python e instalando os pacotes necessários
```shell
python -m venv venv

source venv/bin/activate
pip install -r requirements.txt
```

2. Instalar o banco de dados MySQL ou MariaDB e criar a base de dados/usuário
```sql
create user tanahora identified by 'tanahora';
create database tanahora;
grant all privileges on tanahora.* to tanahora;
```

3. Realizar a migração das tabelas para o banco
No terminal, pasta do projeto:
```shell
source venv/bin/activate
python
```

No python: Cria tabelas a partir do models.py no Banco de dados
```python
from tanahora import db, app_context, Models 
with create_app().app_context():
  db.create_all()

exit()
```

4. Executando
No terminal, pasta do projeto:
```shell
source venv/bin/activate
flask --app tanahora run --debug
```


## :memo: Licença

Esse projeto está sob a licença MIT.

---

Feito com ♥ por alunos da UNIVESP do EIXO de Computação.
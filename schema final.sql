#Drop schema tanahora;
CREATE SCHEMA tanahora;
USE tanahora;



CREATE TABLE responsavel(
id_resp INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
sobrenome VARCHAR(100) NOT NULL,
nick VARCHAR(100) NOT NULL,
datanascimento DATE NOT NULL,
dependentes INT NOT NULL,
telefone VARCHAR(100),
email VARCHAR(100) NOT NULL,
senha VARCHAR(100) NOT NULL,
genero varchar(30) not null);

CREATE TABLE dependente(
id_dep INT PRIMARY KEY AUTO_INCREMENT,
nomed VARCHAR(100) NOT NULL,
sobrenomed VARCHAR(100) NOT NULL,
nickd VARCHAR(100) NOT NULL,
datanascimentod DATE NOT NULL,
telefoned VARCHAR(100),
emaild VARCHAR(100) NOT NULL,
senhad VARCHAR(100) NOT NULL,
generod varchar(30) not null,
id_resp_dep int not null,
FOREIGN KEY (id_resp_dep) REFERENCES responsavel (id_resp));

SELECT * FROM responsavel;
SELECT * FROM dependente;
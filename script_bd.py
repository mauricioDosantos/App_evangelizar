# API do python
import sqlite3

# Função criada na pasta raiz.
from interfaces import *

# Função que cria o banco de dados.
from modulos.classes import *


def criar_bd():
    # conecta ao banco de dados
    conecao = sqlite3.connect('banco_de_dados.db')
    c = conecao.cursor()
    # todo: quando da um erro ele cria o banco de dados pela metade
    # criação das tabelas referente aos agentes do sistema.
    # Cria a tabela Admin
    c.execute('''CREATE table admin(id int AUTO INCREMENT,nome varchar(100),dataNas int,rua varchar(40),numCasa int,
                email varchar(100),senha varchar(30),tst_seguranca varchar(40),PRIMARY KEY(id));''')

    # Cria a tabela Autor
    c.execute('''CREATE table author(id int AUTO INCREMENT,nome varchar(100),dataNas int,
                rua varchar(40),numCasa int,email varchar(100),senha varchar(30),formacao varchar(200),
                assinatura varchar(100),PRIMARY KEY(id));''')

    # Cria a tabela Usuario
    c.execute('''CREATE table user(id int AUTO INCREMENT,nome varchar(100),dataNas int,
                rua varchar(40),numCasa int,email varchar(100),senha varchar(30),PRIMARY KEY(id));''')

    # tabelas que são vinculadas a algum agente do sistema.
    c.execute('''CREATE table post(id int AUTO INCREMENT,id_author int,texto text,dataCri int,dataPub int,
                referencias text,PRIMARY KEY(id),FOREIGN KEY(id_author) references author(id)
                ON DELETE CASCADE);''')

    c.execute('''CREATE table indicated(id int AUTO INCREMENT,id_admin int,
                texto text,referencias text,link text,PRIMARY KEY(id),FOREIGN KEY(id_admin) references admin(id));''')

    c.execute('''CREATE table game(id_user int,id_author int,fase int, pontos int,
                FOREIGN KEY(id_user) references user(id) ON DELETE CASCADE,
                FOREIGN KEY(id_author) references author(id) ON DELETE CASCADE);''')

    c.execute('''CREATE table schedule(id_user int,id_author int,l1c1 varchar(50),l1c2 varchar(50),
    l1c3 varchar(50),l1c4 varchar(50),l1c5 varchar(50),l1c6 varchar(50),l1c7 varchar(50),l2c1 varchar(50),
    l2c2 varchar(50),l2c3 varchar(50),l2c4 varchar(50),l2c5 varchar(50),l2c6 varchar(50),l2c7 varchar(50),
    l3c1 varchar(50),l3c2 varchar(50),l3c3 varchar(50),l3c4 varchar(50),l3c5 varchar(50),l3c6 varchar(50),
    l3c7 varchar(50),l4c1 varchar(50),l4c2 varchar(50),l4c3 varchar(50),l4c4 varchar(50),l4c5 varchar(50),
    l4c6 varchar(50),l4c7 varchar(50),l5c1 varchar(50),l5c2 varchar(50),l5c3 varchar(50),l5c4 varchar(50),
    l5c5 varchar(50),l5c6 varchar(50),l5c7 varchar(50),l6c1 varchar(50),l6c2 varchar(50),l6c3 varchar(50),
    l6c4 varchar(50),l6c5 varchar(50),l6c6 varchar(50),l6c7 varchar(50),
    FOREIGN KEY(id_user) REFERENCES user(id),
    FOREIGN KEY(id_author) REFERENCES author(id));''')
    #  finaliza a conexão
    conecao.commit()
    conecao.close()
    return True


def checa_id(tipo):
    conecao = sqlite3.connect('banco_de_dados.db')
    c = conecao.cursor()

    string = 'SELECT id FROM ' + tipo
    c.execute(string)
    pessoa = c.fetchall()
    conecao.close()
    return len(pessoa[0])


def adicionar_bd(tipo, pessoa):  # todo: DEPOIS FAZER TESTE SE REALMENTE FOI ADICIONADO A PESSOA
    conecao = sqlite3.connect('banco_de_dados.db')
    c = conecao.cursor()

    if tipo == 'user':
        # adiciona os dados
        c.execute('INSERT INTO user(id,nome,dataNas,rua,numCasa,email,senha) VALUES(?,?,?,?,?,?,?);', pessoa)

    elif tipo == 'author':
        c.execute('''INSERT INTO author(id,nome,dataNas,rua,numCasa,email,senha,formacao,assinatura) 
                    VALUES(?,?,?,?,?,?,?,?,?);''', pessoa)

    elif tipo == 'admin':
        c.execute('INSERT INTO admin(id,nome,dataNas,rua,numCasa,email,senha,tst_seguranca) VALUES(?,?,?,?,?,?,?,?);'
                  , pessoa)

    conecao.commit()  # salva o banco de dados

    print('Adicionado com sucesso!')
    conecao.close()


def verificacao(dados):
    conecao = sqlite3.connect('banco_de_dados.db')  # conecta com o banco de dados
    c = conecao.cursor()

    # Consultando banco de dados
    tipos = ('user', 'author', 'admin')
    contador = 0
    for i in range(len(tipos)):
        string = "SELECT email,senha FROM " + tipos[i] + " WHERE email='" + dados[0] + "' AND senha='" + dados[1] + "';"

        c.execute(string)
        pessoa = c.fetchall()
        if len(pessoa) == 1:
            tipo = tipos[i]
            print(pessoa)
            print('Entrando...')
            break

    p = pessoa[0]
    # verifica se a senha ou conta estão no banco de dados
    if tipo == 'user':
        usuario_logado = Usuario(p[0], p[1], p[2], p[3], p[4], p[5], p[6])

    if tipo == 'author':
        usuario_logado = Autor(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

    if tipo == 'admin':
        usuario_logado = Admin(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])

    conecao.close()
    return usuario_logado


def pega_dados(dados):
    conecao = sqlite3.connect('banco_de_dados.db')
    c = conecao.cursor()

    tipos = ('user', 'author', 'admin')
    # pega dados do banco de dados
    for i in range(len(tipos)):
        string = "SELECT * FROM " + tipos[i] + " WHERE email='" + dados[0] + "' AND senha='" + dados[1] + "';"
        c.execute(string)

        pessoa = c.fetchall()
        if len(pessoa) == 1:
            tipo = tipos[i]
            print(pessoa)
            break

    p = pessoa[0]
    print(p)

    # cria objetos com os dados do banco
    if tipo == 'user':
        user_logado = Usuario(p[0], p[1], p[2], p[3], p[4], p[5], p[6])

    if tipo == 'author':
        user_logado = Autor(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

    if tipo == 'admin':
        user_logado = Admin(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])

    conecao.close()
    return user_logado

'''
EXEMPLO DE COMO DEVO FAZER, PARA PASSAR OS DADOS PARA O BANCO DE DADOS,  tupla

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

Para recuperar dados após executar uma instrução SELECT, você pode tratar o cursor como um iterador , 
chamar o fetchone() método do cursor para recuperar uma única linha
correspondente ou chamar fetchall()para obter uma lista das linhas correspondentes.

for row in c.execute('SELECT * FROM stocks ORDER BY price'): #execultar uma consulta ordenando por data
        print(row)

('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
('2006-04-06', 'SELL', 'IBM', 500, 53.0)
('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)
'''

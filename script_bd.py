# API do python
import sqlite3
# Função criada na pasta raiz.
from interfaces import *

# Função que cria o banco de dados.
def criar_bd():
    # conecta ao banco de dados
    conecao = sqlite3.connect('banco_de_dados.db')  # conecta com o banco de dados
    c = conecao.cursor()

    # criação das tabelas referente aos agentes do sistema.
    c.execute('''CREATE table admin(id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar(100),dataNas int,
                rua varchar(40),numCasa int,email varchar(100),senha varchar(30),
                tst_seguranca varchar(40));''')  # Este comando cria a tabela Admin

    c.execute('''CREATE tale author(id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar(100),dataNas int,
                rua varchar(40),numCasa int,email varchar(100),senha varchar(30),formacao varchar(200)
                data_de_inicio int,assinatura varchar(100));''')  # Este comando cria a tabela Autor

    c.execute('''CREATE tale user(id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar(100),dataNas int,
                rua varchar(40),numCasa int,email varchar(100),senha varchar(30));''')

    # tabelas que são vinculadas a algum agente do sistema.
    c.execute('''CREATE table post(id INTEGER PRIMARY KEY AUTOINCREMENT,id_autor int foreign key,texto text,
                dataCri int,dataPub int,referencias text);''')

    c.execute('''CREATE table indicated(id INTEGER PRIMARY KEY AUTOINCREMENT,id_admin int foreign key,
                texto text,referencias text,link text);''')

    conecao.commit()
    conecao.close()
    return True


def adicionar_bd(pessoa):  # DEPOIS FAZER TESTE SE REALMENTE FOI ADICIONADO A PESSOA
    # conecta ao banco de dados
    conecao = sqlite3.connect('banco_de_dados.db')  # conecta com o banco de dados
    c = conecao.cursor()

    # adiciona o dado
    c.execute('INSERT INTO pessoa VALUES(?,?,?,?,?,?,?,?,?);',
              pessoa)  # qual quer erro de não encontrar add, conecao.commit()
    # nome = pessoa[1]
    conecao.commit()  # salva o banco de dados

    print('Adicionado com sucesso!')
    conecao.close()


def consulta_bd():  # exemplo de que o dados deve vir me tupla, palavra = ('RHAT',)
    # conecta ao banco de dados
    conecao = sqlite3.connect('banco_de_dados.db')  # conecta com o banco de dados
    c = conecao.cursor()
    # Consultando banco de dados
    c.execute('SELECT * FROM pessoa;')  # fetchall()para obter uma lista das linhas correspondentes.
    for linha in c.fetchall():  # c.fetchone()
        print(linha)

    conecao.close()


def verificacao(dados):
    conecao = sqlite3.connect('banco_de_dados.db')  # conecta com o banco de dados
    c = conecao.cursor()
    # Consultando banco de dados
    c.execute('SELECT nome,senha FROM pessoa WHERE nome=? and senha=?;', dados[0], dados[1])
    pessoa = c.fetchall()

    # verifica se a senha ou conta estão no banco de dados
    if(dados[0] == pessoa[1] and dados[1] == pessoa[5]):
        print('Verificado com sucesso.')
        print('Entrando.')
        blog()
    else:
        print('Usuário inválido.')

    conecao.close()

# def alterar_bd(nome):


# EXEMPLO DE COMO DEVO FAZER, PARA PASSAR OS DADOS PARA O BANCO DE DADOS,  tupla
##purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
##             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
##             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
##            ]
##c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
##
##Para recuperar dados após executar uma instrução SELECT, você pode tratar o cursor como um iterador , chamar o fetchone()método do cursor para recuperar uma única linha
##correspondente ou chamar fetchall()para obter uma lista das linhas correspondentes.

##for row in c.execute('SELECT * FROM stocks ORDER BY price'): #execultar uma consulta ordenando por data
##        print(row)
##
##('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
##('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
##('2006-04-06', 'SELL', 'IBM', 500, 53.0)
##('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)

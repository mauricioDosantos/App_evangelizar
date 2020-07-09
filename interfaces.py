import time
from script_bd import *
from modulos.classes import *


# Função de introdução do aplicativo.
def tela():
    for i in range(0, 19):
        print('=', end='+')


def boas_vindas():
    tela()
    print('\n')
    time.sleep(1)
    print("           SEJA BEM VINDO(A)!\n")
    time.sleep(1)
    tela()
    print('\n')


# Função menu
def tela_menu():
    tela()
    print('\n   1-Acessar/Cadastrar    2-Jogo')
    tela()
    print('\n   3-Blog                 4-Compartilhar')
    tela()
    print('\n   5-Indicados            6-Cronograma')
    tela()
    print('\n              0-Sair')
    tela()

    op = int(input('\n\nEscolha a Opção: '))
    return op


def tela_cadas_login():
    tela()
    print('\n1-Login     2-Cadastrar\n')
    tela()
    op = int(input('\nOpção: '))

    while op != 1 and op != 2:
        print('Operação inválida!\n')
        op = input('Opção: ')

    if op == 1:
        login()
    if op == 2:
        cadastrar()


# def login():

# Função cadastrar
def cadastrar():
    tipo = input('Tipo de usuário(author, user): ')
    while tipo != 'user' and tipo != 'author' and tipo != 'admin':
        tipo = input('Tipo de usuário(author, user): ')

    if tipo == 'user':
        tela()  # Tela para o usuário
        print('\nPÁGINA DE CADASTRO DO USUÁRIO\n')
        tela()

        nome = input('Nome: ')
        dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        email = input('Digite seu e-mail: ')
        senha = input('Digite uma senha: ')
        rua = input('Rua: ')
        numCasa = int(input('Número da sua casa: '))

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (nome, dataNas, rua, numCasa, email, senha)

    if tipo == 'author':
        tela()
        print('\nPÁGINA DE CADASTRO DO AUTOR\n')
        tela()

        nome = input('Nome: ')
        dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        email = input('Digite seu e-mail: ')
        senha = input('Digite uma senha: ')
        rua = input('Rua: ')
        numCasa = int(input('Número da sua casa: '))
        formacao = input('Qual sua formação?\n')
        assinatura = input('Digite sua assinatura: ')

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (nome, dataNas, rua, numCasa, email, senha, formacao, assinatura)

    if tipo == 'admin':
        tela()
        print('\nPÁGINA DE CADASTRO DO ADMINISTRADOR\n')
        tela()

        nome = input('Nome: ')
        dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        email = input('Digite seu e-mail: ')
        senha = input('Digite uma senha: ')
        rua = input('Rua: ')
        numCasa = int(input('Número da sua casa: '))
        tst_seguranca = input('Algo que só você sabe, para teste de segurança: ')

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (nome, dataNas, rua, numCasa, email, senha, tst_seguranca)

    adicionar_bd(tipo, pessoa)
    print(f'Os dados salvos: {pessoa}')

    return pessoa


def consulta():
    print('======================== CONSULTA ========================')
    # nome = input('Nome: ')
    # print('======================== // ========================\n')
    consulta_bd()
    print('========================== // ============================\n')
    return 0


# Função para entrar no sistema
def login():
    print('======================== LOGIN ========================\n')
    nome = input('Digite nome: ')
    senha = input('Digite senha: ')
    dados = (nome, senha)
    print('========================== // =========================\n')
    verificacao(dados)

    return dados


# Função blog
def blog():
    print('========================== BLOG =========================')
    print('===================== The Frame Blog ====================')
    print('========================== ==== =========================\n\n')
    print('========================== Postagens =========================\n')

    while True:
        print('AINDA NÃO TEMOS BLOG! \n')
        op = int(input('Digite 9 para sair: '))
        if (op == 9):
            # main()
            break

    # para fazer testes, 0 para ilustrar, mas será algum dado do sistema
    return 0

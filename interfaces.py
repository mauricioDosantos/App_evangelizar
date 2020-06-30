import time
from script_bd import *


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
    print('\n   1-Acessar           2-Jogo')
    tela()
    print('\n   3-Blog              4-Compartilhar')
    tela()
    print('\n   5-Indicados         6-Cronograma')
    tela()
    print('\n              0-Sair')
    tela()

    op = int(input('\n\nEscolha a Opção: '))
    return op


# Função cadastrar
def cadastrar():
    pessoa = 0
    print('========================= PÁGINA DE CADASTRO ==========================\n')
    # numero = int(input('número de identificação: '))
    nome = input('Nome: ')
    dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
    email = input('Digite seu e-mail: ')
    senha = input('Digite uma senha: ')
    rua = input('Rua: ')
    numCasa = int(input('Número da sua casa: '))

    pessoa = (nome, dataNas, email, senha, rua, numCasa)
    adicionar_bd(pessoa)
    print('Os dados salvos: {}'.format(pessoa))
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
            main()
            break

    # para fazer testes, 0 para ilustrar, mas será algum dado do sistema
    return 0

from modulos.classes import *
from script_bd import *
from main import *


# Função de introdução do aplicativo.
def boas_vindas():
    print("SEJA BEM VINDO(A)!")

    # para fazer testes, 0 para ilustrar, mas será algum dado do sistema
    return 0


# Função menu
def menu():
    print('================== // ==================')
    print('   1-Acessar             2-Jogo')
    print('================== // ==================')
    print('   3-Blog                4-Compartilhar')
    print('================== // ==================')
    print('   5-Indicados           6-Cronograma')
    print('================== // ==================\n')
    print('                0-Sair')
    print('\n================== // ==================')

    op = int(input('\nEscolha a Opção: '))
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
        if(op == 9):
            main()
            break

    # para fazer testes, 0 para ilustrar, mas será algum dado do sistema
    return 0

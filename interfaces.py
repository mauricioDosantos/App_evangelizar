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
        resultado = login()
    if op == 2:
        resultado = cadastrar()
    return resultado


# Função cadastrar
def cadastrar():
    tipo = input('Tipo de usuário(author, user): ')
    while tipo != 'user' and tipo != 'author' and tipo != 'admin':
        tipo = input('Tipo de usuário(author, user): ')

    identificador = checa_id(tipo)

    if tipo == 'user':
        tela()  # Tela para o usuário
        print('\nPÁGINA DE CADASTRO DO USUÁRIO\n')
        tela()

        usuario_logado = Usuario()
        usuario_logado.nome = input('\nNome: ')
        usuario_logado.dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        usuario_logado.email = input('Digite seu e-mail: ')
        usuario_logado.senha = input('Digite uma senha: ')
        usuario_logado.rua = input('Rua: ')
        usuario_logado.numCasa = int(input('Número da sua casa: '))

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (identificador, usuario_logado.nome, usuario_logado.dataNas, usuario_logado.rua,
                  usuario_logado.numCasa, usuario_logado.email, usuario_logado.senha)

    if tipo == 'author':
        tela()
        print('\nPÁGINA DE CADASTRO DO AUTOR\n')
        tela()

        usuario_logado = Autor()
        usuario_logado.nome = input('\nNome: ')
        usuario_logado.dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        usuario_logado.email = input('Digite seu e-mail: ')
        usuario_logado.senha = input('Digite uma senha: ')
        usuario_logado.rua = input('Rua: ')
        usuario_logado.numCasa = int(input('Número da sua casa: '))
        usuario_logado.formacao = input('Qual sua formação?\n')
        usuario_logado.assinatura = input('Digite sua assinatura: ')

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (identificador, usuario_logado.nome, usuario_logado.dataNas, usuario_logado.rua,
                  usuario_logado.numCasa, usuario_logado.email, usuario_logado.senha, usuario_logado.formacao,
                  usuario_logado.assinatura)

    if tipo == 'admin':
        tela()
        print('\nPÁGINA DE CADASTRO DO ADMINISTRADOR\n')
        tela()

        usuario_logado = Admin()
        usuario_logado.nome = input('\nNome: ')
        usuario_logado.dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
        usuario_logado.email = input('Digite seu e-mail: ')
        usuario_logado.senha = input('Digite uma senha: ')
        usuario_logado.rua = input('Rua: ')
        usuario_logado.numCasa = int(input('Número da sua casa: '))
        usuario_logado.tst_seguranca = input('Algo que só você sabe, para teste de segurança: ')

        # todo: estes itens seram adicionados a classe e da classe para o banco de dados, no futuro
        pessoa = (identificador, usuario_logado.nome, usuario_logado.dataNas, usuario_logado.rua,
                  usuario_logado.numCasa, usuario_logado.email, usuario_logado.senha, usuario_logado.tst_seguranca)

    adicionar_bd(tipo, pessoa)
    print(f'Os dados salvos: {pessoa}')

    return usuario_logado


# Função para entrar no sistema
def login():
    print('======================== LOGIN ========================\n')
    email = input('Digite email: ')
    senha = input('Digite senha: ')
    dados = (email, senha)
    print('========================== // =========================\n')
    resultado = verificacao(dados)
    if resultado:
        usuario = pega_dados(dados)

    return usuario


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

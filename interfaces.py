#import os
from modulos.classes import *
from script_bd import *
from main import *

def boas_vindas():
    print("SEJA BEM VINDO(A)!")#fazer algo para dar introdução ao app

def menu():
    #os.sytem('cls')
    print('================== // ==================')#acessar, e depois mostra se login ou cadastrar
    print('   1-Acessar             2-Jogo')#no perfil, pode alterar, e enviar email
    print('================== // ==================')
    print('   3-Blog                4-Compartilhar')#no blog se entrar sem acessar ele apenas ver as postagens
    print('================== // ==================')
    print('   5-Indicados           6-Cronograma')#indicados são sites e apps sugestões para acessarem.
    print('================== // ==================\n')#lista cadas para o admin
    print('                0-Sair')#indicados são sites e apps sugestões para acessarem.
    print('\n================== // ==================')#lista cadas para o admin

    op = int(input('\nEscolha a Opção: '))
    return op

def cadastrar():
    #os.sytem('cls')
    pessoa = 0
    print('========================= PÁGINA DE CADASTRO ==========================\n')

    numero = int(input('nº: '))
    nome = input('Nome: ')
    acredita = bool(input('Você tem fé?(0 para falso ou 1 para verdadeiro): '))
    igreja = input('Você frequenta qual igreja? ')
    aceita = bool(input('Podemos lhe visitar?(0 para falso ou 1 para verdadeiro): '))
    dataNas = int(input('Sua data de nascimento é *Obs: sem barra, só o número: '))
    senha = input('Digite uma senha: ')
    rua = input('Rua: ')
    numCasa = int(input('Número da sua casa: '))

    pessoa = (numero,nome,acredita,igreja,aceita,dataNas,senha,rua,numCasa)#tupla que recebe os valores
    adicionar_bd(pessoa)#lista que recebe as tuplas, que irão ser adicionadas no banco de dados

    print('Os dados salvos: {}'.format(pessoa))
    return pessoa

def consulta():
    #os.system('cls')
    print('======================== CONSULTA ========================')
    #nome = input('Nome: ')
    #print('======================== // ========================\n')
    consulta_bd()
    print('========================== // ============================\n')

def login():
    #ferificar se tem essa conta no banco de dados, nome e senha
    #setiver ele entra e vai para o blog
    #na aba blog ele apenas ver os postes
    print('======================== LOGIN ========================\n')
    nome = input('Digite nome: ')
    senha = input('Digite senha: ')
    dados = (nome,senha)
    print('========================== // =========================\n')
    varificacao(dados)

def blog():
    print('========================== BLOG =========================')
    print('===================== The Frame Blog ====================')
    print('========================== ==== =========================\n\n')
    print('========================== Postagens =========================\n')
    #consultar banco de dados de postagem, deve ter pessoa asociada 
    
    while(True):
        print('AINDA NÃO TEMOS BLOG! \n')
        op = int(input('Digite 9 para sair: '))
        if(op == 9):
            main()


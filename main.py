# -*- coding: utf-8 -*-
# Arquivo principal
# por mauricioDosantos
# versão 0.1
from modulos.classes import *
from interfaces import *
from script_bd import *
import sqlite3
import os.path


# caso não tenha nem um banco de dados, função para criar
def main():

    while True:
        # checa se na pasta tem o arquivo: 'banco_de_dados.db'
        if os.path.isfile('banco_de_dados.db'):
            print('Carregamento feito com sucesso!\n')
        else:
            # função para criar um banco de dados e suas tabelas
            c = criar_bd()

        op = tela_menu()
        
        if op == 1:
            login()
        elif op == 2:
            cadastrar()  # cadastra e retorna um objeto adicionado na classe Pessoa
        elif op == 3:
            print("Infelizmente essa função ainda não foi criada!")
        elif op == 4:
            print("Infelizmente essa função ainda não foi criada!")
        elif op == 5:
            print("Infelizmente essa função ainda não foi criada!")
        elif op == 6:
            print("Infelizmente essa função ainda não foi criada!")
        elif op == 0:
            print('Fim de execução do programa...')
            break;


main()

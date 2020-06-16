#Arquivo principal
#-*- coding: utf-8 -*-
from modulos.classes import *
from interfaces import *
from script_bd import *
from main import *
import sqlite3
import os.path


estado = True
#caso não tenha nem um banco de dados, função para criar
def main():
    while(estado):
        if(os.path.isfile('banco_de_dados.db')):#checa se na pasta tem o arquivo: 'banco_de_dados.db'
            print('Carregamento feito com sucesso!\n')
        else:
            c = criar_bd()#função para criar um banco de dados e suas tabelas
            
        op = menu()#Chama o menu inicial
        
        if op == 1:
            login()
        elif op == 2:
            pessoa = cadastrar()#cadastra e retorna um objeto adicionado na classe Pessoa
        elif op == 3:
            print ("Infelizmente essa função ainda não foi criada!")
        elif op == 4:
            print ("Infelizmente essa função ainda não foi criada!")
        elif op == 5:
            print ("Infelizmente essa função ainda não foi criada!")
        elif op == 6:
            print ("Infelizmente essa função ainda não foi criada!")
        elif op == 8:
            print ("Infelizmente essa função ainda não foi criada!")
        elif op == 9:
            consulta()#lista todos os campos do banco de dados
        elif op == 10:
            print('PROGRAMA FECHADO.')
            break;

main()

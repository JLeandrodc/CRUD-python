# Programador J.Leandro
# R.A 2221032
import os
from time import *
from datetime import datetime # mostrar a data de abertura
import pytz #biblioteca de fuso horario
import funcoes #importa as funções que estão em outro arquivo py
#--------------------------------------------------------------------------------------------------------------
fusoHorario = pytz.timezone('America/Sao_Paulo')# fuso horaio
horaAtual = datetime.now(fusoHorario).strftime("%H:%M:%S") # hora e formatação de hora
data = (datetime.now())  # registra a data atual
date = f' {data.day}/{data.month}/{data.year}'  # formatação da data para o Brasil
numerodoLog = []
#--------------------------------------------------------------------------------------------------------------
def menu():
    respmenuCRUD = "SIM"
    while respmenuCRUD == "SIM":
        print ("Olá, Seja bem vindo !!!" '\n')
        print (f'{"Qual opção você deseja ?"} \n'
        f' {"1 - Consultar protocolo"} \n'
        f' {"2 - Registrar protocolo"} \n'
        f' {"3 - Editar protocolo"} \n'
        f' {"4 - Excluir protocolo"} \n'
        f' {"5 - MTC do protocolo"} \n'
        f' {"6 - Log do protocolo"}\n'
        f' {"7 - Voltar ao menu principal"}')
        entrada = input ("")
        if entrada == "1":
            os.system ("clear")
            with open('log.txt', 'a') as log: # Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Consulta"}; data:{date}; Hora:{horaAtual}')# Registra a ação
            funcoes.consultaCliente()
        elif entrada == "2":
            os.system ("clear")
            with open('log.txt', 'a') as log:# Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()# gera numero do log
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Registro"}; data:{date}; Hora:{horaAtual}')# Registra a ação
            funcoes.registro()
        elif entrada == "3":
            os.system ("clear")
            with open('log.txt', 'a') as log:# Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()# gera numero do log
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Editar"}; data:{date}; Hora:{horaAtual}')# Registra a ação
            funcoes.editar()
        elif entrada == "4":
            os.system ("clear")
            with open('log.txt', 'a') as log:# Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()# gera numero do log
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Excluir"}; data:{date}; Hora:{horaAtual}')# Registra a ação
            funcoes.excluir()
        elif entrada == "5":
            os.system ("clear")
            with open('log.txt', 'a') as log:# Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()# gera numero do log
                log.write(f'Usuário: {"José Leandro"}; Ação: {"MTC"}; data:{date}; Hora:{horaAtual}')# Registra a ação
            funcoes.MTC()
        elif entrada == "6":
            os.system("clear")
            with open ('log.txt','a') as log:# Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()# gera numero do log
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Log"}; data:{date}; Hora:{horaAtual}')# Registra a ação
                funcoes.excluirLog()
        elif entrada == "7":
            respmenuCRUD=""
            os.system("clear")
            respmenu="SIM"
        else:
            os.system("clear")
            print ("Opção invalida (╥﹏╥)" "\n")
            respmenuCRUD = "SIM"
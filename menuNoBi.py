# Programador J.Leandro
# R.A 2221032
import os # limpa o console
from time import *# importa a hora
from datetime import datetime # mostrar a data de abertura
import pytz #biblioteca de fuso horario
import normaleBinomial #importa as funções que estão em outro arquivo py
import funcoes #importa as funções que estão em outro arquivo py
#--------------------------------------------------------------------------------------------------------------
fusoHorario = pytz.timezone('America/Sao_Paulo')# fuso horaio
horaAtual = datetime.now(fusoHorario).strftime("%H:%M:%S") # hora e formatação de hora
data = (datetime.now())  # registra a data atual
date = f' {data.day}/{data.month}/{data.year}'  # formatação da data para o Brasil
numerodoLog = []
#--------------------------------------------------------------------------------------------------------------
def menu():
    respmenuNoBi = "SIM"
    while respmenuNoBi =="SIM":
        os.system("clear")
        print ("Olá, Seja bem vindo !!!" '\n')
        print (f'{"Qual opção você deseja ?"} \n'
        f' {"1 - Problema binomial e normal fixo"} \n'
        f' {"2 - Binomial com entrada de dados"} \n'
        f' {"3 - Voltar ao menu principal"}')
        entrada = input ("")
        if entrada == "1":
            os.system ("clear")
            with open('log.txt', 'a') as log: # Registra a ação
                numerodoLog = funcoes.gerarNumeroDoLog()
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Problema binomial e normal fixo"}; data:{date}; Hora:{horaAtual}')# Registra a ação
                normaleBinomial.valoresProbabilidade()
        elif entrada == "2":
            os.system("clear")
            with open('log.txt', 'a') as log:
                numerodoLog = funcoes.gerarNumeroDoLog()
                log.write(f'Usuário: {"José Leandro"}; Ação: {"Binomial com entrada de dados"}; data:{date}; Hora:{horaAtual}')
                normaleBinomial.entradasBinomial()
        elif entrada == "3":
            respmenuNoBi=""
            os.system("clear")
            respmenu="SIM"
        else:
            os.system("clear")
            print ("Opção invalida (╥﹏╥)")
            respmenuNoBi = "SIM"
import menuCRUD
import statistics #Importa algumas funções do MTC
import os  # biblioteca para limpar o console
from time import *
from datetime import datetime # mostrar a data de abertura
import pytz #biblioteca de fuso horario
import funcoes #importa as funções que estão em outro arquivo py
import math #importa as funções para o binomial
#------------------------------------------------------------------------------------------------------------------
fusoHorario = pytz.timezone('America/Sao_Paulo')# fuso horaio
horaAtual = datetime.now(fusoHorario).strftime("%H:%M:%S") # hora e formatação de hora
data = (datetime.now())  # registra a data atual
date = f' {data.day}/{data.month}/{data.year}'  # formatação da data para o Brasil
linha = '_' * 114
protocolo = [] # Abaixo, são listas dos dados necessarios para a abertura de um processo
assunto = []
requerente = []
historico = []
operador = []
setor = []
log = []
#--------------------------------------------------------------------------------------------------------------
def lerDados():
    bancodeDados = "2022.txt"
    lista = []
    with open(bancodeDados, "r") as f:
        linhas = f.readlines()
    for linha in linhas:
        dados = linha.strip().split(";")
        lista.append(dados)
    return lista
#--------------------------------------------------------------------------------------------------------------
def escreverDados(listaTemporaria):
    bancodeDados = "2022.txt"
    with open(bancodeDados, "a") as f:
        for i in listaTemporaria:
            f.write(str(i) + ";")
#--------------------------------------------------------------------------------------------------------------
def cabeçalhoSimples():  # cabeçalho basico da visão do cliente, contendo as informações basicas do processo
    print(f'{"Protocolo Nº":<0} {protocolo[0]:<0} {"data da consulta: ":>40} {date:>0}\n{linha}\n{"Unidade de origem: ":>0} {setor[0]:>0}\n'
    f'{linha}\n{"Assunto: ":>0} {assunto[0]:>0}\n{linha}\n{"Funcionario responsavel: ":>0} {operador[0]:>0}\n{linha}\n'
    f'{"Requerente: ":>0} {requerente[0]:>0}\n{linha}\n{"Descrição do problema: ":>0} {historico[0]:>0}\n{linha}\n')
#--------------------------------------------------------------------------------------------------------------
def consultaCliente():#codigo para a consulta do processo, isso na visão do cliente
    try:
        respConsulta = "SIM"
        while respConsulta == "SIM":
            os.system("clear")
            num = input("Digite o numero do processo: ")
            os.system('clear')
            while not num.isdigit():
                num = input("numero invalido, digite novamente: ")
                os.system('clear')
            ano = input("Digite o ano do processo: ")
            os.system('clear')
            cont = 0
            while not ano.isdigit:
                ano = input('Ano invalido, digite novamente: ')
                os.system('clear')
            if ano == "2022":
                listadedados = open("2022.txt", "r")#abre um arquivo txt, o 'r' seria o modo de abertura, r=leitura
                dados = []
                for i in listadedados:#faz a leitura dos dados em txt
                    dados.append(i.rstrip().split(";"))#tira um caractere a direita, o espaço por exemplo, e sepra quando encontra o ;
                for i in dados:
                    for valor in i:
                        if num == valor:
                            cont = 1
                            protocolo.append(i[0])  # esse é o index da lista, a posição que cada um se encontra
                            requerente.append(i[1])  # nome do requerente
                            assunto.append(i[2])  # nome do assunto
                            historico.append(i[3])  # informaçãoes do problema
                            operador.append(i[4])  # nome do operador
                            setor.append(i[5])  # setor de abertura do processso
                            break  # sair do loop assim que o processo for encontrado
            if cont != 0:
                cabeçalhoSimples()
                break
            else:
                print("Não foi encontrado nenhum processo com esse protocolo")
                print("Deseja editar outro protocolo?")
                respConsulta = input("").upper()
        print("Obrigado por usar o PROTO-ON")
    except:
        print ("Ops, ocorreu um erro inesperado, desculpe pelo incoviniente")
        print ("Gostaria de ultilizar o sistema novamente?")
        respConsulta = input("").upper
        menuCRUD.menu()

#--------------------------------------------------------------------------------------------------------------
def MTC(): # calculo de medidas tentenciais
    dados = lerDados()
    operadores = [] # Usei os operadores para fazer os calculos (José Leandro e Luis)
    contagens = []
    for linhaLista in dados:
        linha = linhaLista[4]  # pega o nome do operador da lista de dados, para usar como base nos calculos do MTC
        if linha in operadores:
            indice = operadores.index(linha)
            contagens[indice] += 1
        else:
            operadores.append(linha)
            contagens.append(1)
    media = sum(contagens) / len(contagens)
    moda = statistics.mode(contagens)
    mediana = statistics.median(contagens)
    variancia = statistics.variance(contagens)
    desvioPadrao = statistics.stdev(contagens)
    print(f'{"Média de processos abertos por operador:"} {media} \n'
    f'{"Moda de processos abertos por operador:"} {moda} \n'
    f'{"Mediana de processos abertos por operador:"} {mediana} \n'
    f'{"Variância de processos abertos por operador:"} {variancia} \n'
    f'{"Desvio padrão de processos abertos por operador:"} {desvioPadrao} \n')
    n = input("Presione enter para voltar ao menu")
    os.system("clear")
    menuCRUD.menu()
#--------------------------------------------------------------------------------------------------------------
def gerarProtocolo():# função principal da geração de protocolos
    ultimoProtocolo = lerUltimoProtocolo()
    novoProtocolo = incrementarProtocolo(ultimoProtocolo)
    escreverUltimoProtocolo(novoProtocolo)
    return novoProtocolo
#--------------------------------------------------------------------------------------------------------------
def lerUltimoProtocolo():#Lê o ultimo protocolo registrado
    try:
        with open("2022.txt", "r") as f:
            linhas = f.readlines()
            if linhas:
                ultimoProtocolo = linhas[-1].rstrip('\n').split(";")[0]
                return ultimoProtocolo
            else:
                ultimoProtocolo = '0'
                return ultimoProtocolo
    except FileNotFoundError:
        return "000"
#--------------------------------------------------------------------------------------------------------------
def incrementarProtocolo(protocolo):# Gera um numero de protocolo a partir do ultimo registrado
    if protocolo.isdigit():
        numero = int(protocolo)
    else:
        numero = 0
    numero += 1
    novoProtocolo = str(numero).zfill(3)# zfill() é um método de string em Python que preenche uma string com zeros à esquerda para alcançar um determinado número de dígitos
    return novoProtocolo
#--------------------------------------------------------------------------------------------------------------
def escreverUltimoProtocolo(protocolo):
    with open("2022.txt", "a") as f:
        f.write("\n"+ protocolo + ";")
#--------------------------------------------------------------------------------------------------------------
def registro():# função para registrar o processo
    try:
        respRegistro = "SIM"
        while respRegistro== "SIM":
            protocolo = gerarProtocolo()
            listaTemporaria = [] # salva os dados do registro temporariamente
            print ("Protocolo: " + protocolo)
            #listaTemporaria.append(protocolo)
            print ("Digite o nome do municipe")
            n = input ("")
            listaTemporaria.append(n)
            os.system("clear")
            print ("Qual o assunto?")
            n= input ("")
            listaTemporaria.append(n)
            os.system("clear")
            print ("Digite o relato do requerente")
            n= input ("")
            listaTemporaria.append(n)
            listaTemporaria.append("José Leandro")
            listaTemporaria.append("GESTÃO DOCUMENTAL")
            os.system("clear")
            escreverDados(listaTemporaria)
            os.system("clear")
            print("Processo registrado com sucesso!")
            print ("Deseja realizar outro registro?")
            respRegistro = input("").upper()
            os.system("clear")
            menuCRUD.menu()
    except:
        print ("Ops, ocorreu um erro inesperado, desculpe pelo incoviniente")
        print ("Gostaria de registrar um processo?")
        respRegistro = input("").upper
        menuCRUD.menu()
#--------------------------------------------------------------------------------------------------------------
def sobrescreverItem(arquivo, indice, novaInformacao): # sobrescreve algum item do processo
    with open("2022.txt", "r") as f:
        linhas = f.readlines()

    if indice < 0 or indice >= len(linhas):
        print("Índice inválido.")
        return

    linhas[indice] = novaInformacao + '\n'

    with open("2022.txt", 'w') as f:
        f.writelines(linhas)
#--------------------------------------------------------------------------------------------------------------
def editar():  # função de editar um processo
    try:
        respEditar = "SIM"
        while respEditar == "SIM":
            print("Qual processo deseja editar?")
            n = input("")
            os.system("clear")
            while not n.isdigit():
                print("Digite somente os números")
                n = input("")
                os.system("clear")
            print("Qual o ano do processo?")
            f = input("")
            os.system("clear")
            while not f.isdigit():
                print("Digite apenas números")
                f = input("")
                os.system("clear")
            if f == "2022":
                arquivo = "2022.txt"
                listadedados = lerDados()
                cont = 0
                for i, dados in enumerate(listadedados):
                    if dados[0] == n:
                        cont = 1
                        protocolo = dados[0]
                        requerente = dados[1]
                        assunto = dados[2]
                        historico = dados[3]
                        operador = dados[4]
                        setor = dados[5]
                        break
        
                if cont != 0:
                    while respEditar == "SIM":
                        print("O que deseja alterar?")
                        print("1 - Requerente")
                        print("2 - Assunto")
                        print("3 - Histórico")
                        opcao = input("")
                        os.system("clear")
                        if opcao == "1":
                            print("Digite o nome do requerente:")
                            r = input("")  # Input de entrada de dados
                            listadedados[i][1] = r  # Atualizar o nome do requerente no registro
                            novaInformacao = ';'.join(listadedados[i])
                            sobrescreverItem(arquivo, i, novaInformacao)
                            os.system("clear")
                            print("Processo atualizado com sucesso!")
                            print("Deseja fazer mais alguma alteração no processo nº " + n + "/" + f + "?")
                            respEditar = input("").upper()
                            os.system("clear")
                        elif opcao == "2":
                            print("Digite assunto do processo:")
                            r = input("")  # Input de entrada de dados
                            listadedados[i][2] = r  # Atualizar o nome do requerente no registro
                            novaInformacao = ';'.join(listadedados[i])
                            sobrescreverItem(arquivo, i, novaInformacao)
                            os.system("clear")
                            print("Processo atualizado com sucesso!")
                            print("Deseja fazer mais alguma alteração no processo nº " + n + "/" + f + "?")
                            respEditar = input("").upper()
                            os.system("clear")
                        elif opcao == "3":
                            print("Digite o histórico do processo:")
                            r = input("")  # Input de entrada de dados
                            listadedados[i][3] = r  # Atualizar o nome do requerente no registro
                            novaInformacao = ';'.join(listadedados[i])
                            sobrescreverItem(arquivo, i, novaInformacao)
                            os.system("clear")
                            print("Processo atualizado com sucesso!")
                            print("Deseja fazer mais alguma alteração no processo nº " + n + "/" + f + "?")
                            respEditar = input("").upper()
                            os.system("clear")
                        else:
                            print("Opção inválida!" "\n")
                            respEditar = "SIM"
                else:
                    print("Não foi encontrado nenhum processo com esse Nº de protocolo")
                    print("Deseja editar outro protocolo?")
                    respEditar = input("").upper()
                    os.system("clear")
        menuCRUD.menu()
    except:
        print("Ops, ocorreu um erro inesperado, desculpe pelo incômodo")
        print("Gostaria de editar um processo?")
        respEditar1 = input("").upper()
        menuCRUD.menu()
#--------------------------------------------------------------------------------------------------------------
def excluirLinha(arquivo, entrada): # exclui um processo
    with open("2022.txt", 'r') as f:
        linhas = f.readlines()
    linhaEncontrada = False
    for i, linha in enumerate(linhas):
        dados = linha.split(';')
        if dados[0].strip() == entrada:
            del linhas[i]
            linhaEncontrada = True
            break
    if linhaEncontrada:
        with open("2022.txt", 'w') as f:
            f.writelines(linhas)
        print("Processo excluído com sucesso.")
    else:
        print("Não foi encontrado nenhum processo com esse Nº de protocolo.")
#--------------------------------------------------------------------------------------------------------------
def excluir(): # função de excluir um processo
    respExcluir = "SIM"
    while respExcluir == "SIM":
        print("Qual processo deseja excluir?")
        entrada = input("")
        os.system("clear")
        while not entrada.isdigit():
            print("Digite somente os números")
            entrada = input("")
            os.system("clear")
        print("Qual o ano do processo?")
        f = input("")
        os.system("clear")
        while not f.isdigit():
            print("Digite apenas números")
            f = input("")
            os.system("clear")
        if f == "2022":
            arquivo = "2022.txt"
            excluirLinha(arquivo, entrada)
        else:
            print("Não foi encontrado nenhum processo com esse Nº de protocolo")

        print("Deseja excluir outro protocolo?")
        respExcluir = input("").upper()
        os.system("clear")
    menuCRUD.menu()

#--------------------------------------------------------------------------------------------------------------
def gerarNumeroDoLog():
    ultimoNumeroDoLog = lerUltimoNumeroDoLog()
    novoNumeroDoLog = incrementarNumeroDoLog(ultimoNumeroDoLog)
    escreverUltimoNumeroDoLog(novoNumeroDoLog)
    return novoNumeroDoLog
#--------------------------------------------------------------------------------------------------------------
def lerUltimoNumeroDoLog():
    try:
        with open("log.txt", "r") as f:
            linhas = f.readlines()
            if linhas:
                ultimoNumeroDoLog = linhas[-1].rstrip('\n').split(";")[0]
                return ultimoNumeroDoLog
            else:
                ultimoNumeroDoLog = '0'
                return ultimoNumeroDoLog
    except FileNotFoundError:
        return "000"
#--------------------------------------------------------------------------------------------------------------
def incrementarNumeroDoLog(numeroDoLog):
    if numeroDoLog.isdigit():
        numero = int(numeroDoLog)
    else:
        numero = 0
    numero += 1
    novoNumeroDoLog = str(numero).zfill(3)
    return novoNumeroDoLog
#--------------------------------------------------------------------------------------------------------------
def escreverUltimoNumeroDoLog(numeroDoLog):
    with open("log.txt", "a") as f:
        f.write("\n" + numeroDoLog + ";")
#--------------------------------------------------------------------------------------------------------------
def excluirLinhaLog(log, entrada): # exclui um processo
    with open("log.txt", "r") as f:
        linhas = f.readlines()
    linhaEncontrada = False
    for i, linha in enumerate(linhas):
        dados = linha.split(';')
        if dados[0].strip() == entrada:
            del linhas[i]
            linhaEncontrada = True
            break
    if linhaEncontrada:
        with open("log.txt", 'w') as f:
            f.writelines(linhas)
        print("Linha excluída com sucesso.")
    else:
        print("Não existe nenhum historico com nessa linha.")
#--------------------------------------------------------------------------------------------------------------
def excluirLog(): # função de excluir um processo
    respExcluirLog = "SIM"
    while respExcluirLog =='SIM':
        with open("log.txt", "r") as f:
            linhas = f.readlines()
        for linha in linhas:# Imprime o conteúdo do arquivo no console
            print(linha, end='')
        print ("\n \nDigite (1) se deseja excluir somente uma linha, e (2) para excluir o histórico completo")
        entrada = input("")
        if entrada == "1":
            os.system("clear")
            respExcluirLogLinha = "SIM"
            respExcluirLog = ""
            while respExcluirLogLinha == "SIM":
                for linha in linhas:# Imprime o conteúdo do arquivo no console
                    print(linha, end='')
                print("\n""Qual linha deseja excluir?")
                entrada = input("")
                os.system("clear")
                while not entrada.isdigit():
                    print("Digite somente os números")
                    entrada = input("")
                    os.system("clear")
                log = "log.txt"
                excluirLinhaLog(log, entrada)
                print("Deseja excluir outra linha?")
                respExcluirLogLinha = input("").upper()
                os.system("clear")
        elif entrada=="2":
            os.system("clear")
            print("Tem certeza que deseja apagar todos os registros? (s/n): ")
            entrada = input("")
            if entrada.lower() == "s":
                with open("log.txt", "w") as f:
                    f.write("")
                os.system("clear")
                print(f'{"Registros apagados com sucesso!"} \n'
                f'{"Deseja excluir alguma informação do log?"}')
                respExcluirLog = input("").upper()
                os.system("clear")
            else:
                os.system("clear")
                print(f'{"Operação de apagar registros cancelada."} \n'
                f'{"Deseja excluir alguma informação do log?"}')
                respExcluirLog = input("").upper()
                os.system("clear")
        else:
            os.system("clear")
            print(f'{"Opção invalida!"} \n'
            f'{"Deseja excluir alguma informação do log?"}')
            respExcluirLog = input("").upper()
            os.system("clear")
    menuCRUD.menu()
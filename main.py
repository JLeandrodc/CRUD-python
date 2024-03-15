# Programador J.Leandro
# R.A 2221032
# Dados sem nenhuma base real, apenas para fins de programação.
import menuCRUD
import menuNoBi
import sys
import os
#--------------------------------------------------------------------------------------------------------------
entrada=""
respmenu="SIM"
while respmenu=="SIM":
    print(f'{"Olá professor Luis"} \n'
        f'{"O que o senhor deseja testar?"} \n'
        f'{"1 - CRUD"} \n'
        f'{"2 - Normal e Binomial"}\n'
        f'{"3 - Sair"}')
    entrada = input("")
    if entrada == "1":
        os.system("clear")
        menuCRUD.menu()
    elif entrada == "2":
        os.system("clear")
        menuNoBi.menu()
    elif entrada == "3":
        os.system("clear")
        print("Obrigado por usar o PROT-ON")
        exit()
    else:
        os.system("clear")
        print ("Opção invalida (╥﹏╥)" "\n")
        respmenu="SIM"

import math
import os
import menuNoBi
linha = 130*"_"
#--------------------------------------------------------------------------------------------------------------
def calcularProbabilidade(n, p, k, distribuicao):
    if distribuicao == 'binomial':
        q = 1 - p
        comb = math.comb(n, k)
        prob = comb * (p ** k) * (q ** (n - k))
        probDecimal = round(prob, 9)  # Resultado decimal com 9 casas decimais
        probPorcentagem = round(prob * 100, 2)  # Resultado em porcentagem com 2 casas decimais
        print(f"(Modelo Binomial) A probabilidade de mais de {k} processos estarem corretamente preenchidos é de {probDecimal} ou {probPorcentagem}%. \n")
    elif distribuicao == 'normal':
        media = n * p
        desvioPadrao = math.sqrt(n * p * (1 - p))
        z = (k - media) / desvioPadrao
        prob = (1 / (desvioPadrao * math.sqrt(2 * math.pi))) * math.exp(-0.5 * z**2)
        probDecimal = round(prob, 9)  # Resultado decimal com 9 casas decimais
        probPorcentagem = round(prob * 100, 2)  # Resultado em porcentagem com 2 casas decimais
        print(f"(Modelo Normal) A probabilidade de mais de {k} processos estarem corretamente preenchidos é de {probDecimal} ou {probPorcentagem}%. \n")
    else:
        raise ValueError("Distribuição inválida. Escolha 'binomial' ou 'normal'.")
#--------------------------------------------------------------------------------------------------------------
def valoresProbabilidade():
    print(f'{"Questão:"} \n'
    f'{"Qual é a probabilidade de que, em uma amostra de 100 processos administrativos de uma prefeitura,"} \n'
    f'{"mais de 70 deles estejam corretamente preenchidos?"}\n' + linha + '\n')
    n = 100  # número de processos administrativos
    p = 0.7  # probabilidade de um processo estar corretamente preenchido
    k = 70   # número mínimo de processos corretamente preenchidos
    calcularProbabilidade(n, p, k, 'binomial')
    calcularProbabilidade(n, p, k, 'normal')
    entrada=input("Aperte enter para voltar ao menu")
    os.system("clear")
    menuNoBi.menu()
#--------------------------------------------------------------------------------------------------------------    
def binomial(p, n, k):
    if k < 0 or k > n:
        return 0
    resultado = 1
    for i in range(1, k+1):
        resultado *= (n - i + 1)
        resultado //= i
    resultado *= p ** k
    resultado *= (1 - p) ** (n - k)
    return resultado
#--------------------------------------------------------------------------------------------------------------
def verFloat(valor): # Verificar se é float, para não travar o programa
    try:
        float(valor)
        return True
    except:
        return False
#--------------------------------------------------------------------------------------------------------------
def entradasBinomial():
    print("Digite o valor de P:")
    p = input()
    os.system("clear")
    while not verFloat(p):
        print("Valor inválido. Digite novamente o valor de P:")
        p = input()
        os.system("clear")
    p = float(p)
    os.system("clear")
    print("Digite o valor de N:")
    n = input()
    os.system("clear")
    while not n.isdigit():
        print("Valor inválido. Digite novamente o valor de N:")
        n = input()
        os.system("clear")
    n = int(n)
    os.system("clear")
    print("Digite o valor de K:")
    k = input()
    os.system("clear")
    while not k.isdigit():
        print("Valor inválido. Digite novamente o valor de K:")
        k = input()
        os.system("clear")
    k = int(k)
    os.system("clear")
    resultado = binomial(p, n, k)
    print("A probabilidade binomial de P:{}, N:{} e K:{}, é de: {}".format(p, n, k, resultado))
    entrada = input("Aperte enter para voltar ao menu")
    os.system("clear")
    menuNoBi.menu()

    


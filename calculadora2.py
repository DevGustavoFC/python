
'''
|==============================================|
|==============================================|
|Programa criado para fins de matemática básica|
|==============================================|
|==============================================|
'''

import math
from math import pi
from datetime import date
import sys



print("""
    MUITO BEM VINDO AO "PROGRAMA DE MATEMÁTICA BÁSICA" NELE 
    ESTAREMOS VENDO CONCEITOS PARA RESOLUÇÃO DE PROBLEMAS
    DE MATEMÁTICA BÁSICA.
    
Primeiro Projeto (de grau introdutório) em Python.""", date.today())


def menu_inicial():
    print("""
        CATÁLOGO DE OPÇÕES

        1- CALCULADORA BÁSICA (ADIÇÃO/SUBTRAÇÃO/MULTIPLICAÇÃO/DIVISÃO)
        2- CALCULADORA DE PORCENTAGEM
        3- CALCULADORA DE PROBABILIDADE
        4- MÉDIA ARITMÉTICA
        5- SAIR
    """)

while True:
    comprimento = 80
    linha = "-" * comprimento
    print("{0}".format(linha))
    
    menu_inicial()
    resposta_menu_inicial = str(input('Digite a opção: '))

    if resposta_menu_inicial == '1':

        while True:         
            print("""

            Bem-vindo à Calculadora Básica: 

            """)
            print("Selecione a operação desejada:")
            print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Voltar\n")

            opcao = input("Digite uma das opções: ")

            if opcao == '1':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                soma = num1+num2
                print(num1, "+", num2, "=", soma)

            elif opcao == '2':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                subtracao = num1-num2
                print(num1, "-", num2, "=", subtracao)

            elif opcao == '3':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                multiplicacao = num1*num2
                print(num1, "*", num2, "=", multiplicacao)

            elif opcao == '4':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                divisao = num1/num2
                print(num1, "/", num2, "=", divisao)

            elif opcao == '5':
                print("Retornando ao menu inicial...")
                break

            else:
                print("Opção Inválida, insira outro valor.")
                

    elif resposta_menu_inicial == '2':
        print("""

            Bem-vindo à Calculadora de Porcentagem

            """)

        valor_total = float(input("Digite o valor total: "))
        percentual = float(input("Digite o percentual (%): "))
        resultado = valor_total * (percentual/100)
        print("O resultado é:", resultado)

    elif resposta_menu_inicial == '3':
        print("""

            Bem-vindo à Calculadora de Probabilidade

            """)


        evento = int(input("Digite o número de eventos: "))
        espaco_amostral = int(input("Digite o tamanho do espaço amostral: "))
        probabilidade = evento/espaco_amostral
        print("A probabilidade é:", probabilidade)


    elif resposta_menu_inicial == '4':
        print("""

            Bem vindo à Calculadora de Média Aritmética

            """)

        num_valores = int(input("Quantos números você deseja inserir na lista? "))

        valores = []

        for i in range(num_valores):
            valor = float(input("Digite o valor {}: ".format(i+1)))
            valores.append(valor)

            soma = sum(valores)
            media = soma / num_valores

            print("A média aritmética dos valores inseridos é: {}".format(media))
            

    elif resposta_menu_inicial == '5':
        print("""

            Muito obrigado por utilizar do meu primeiro projeto em Python!
            Em breve será disponibilizado um outro projeto de nível semelhante
            ou superior a este. 

            [CALCULADORA FECHADA]
            
        """)
        sys.exit()

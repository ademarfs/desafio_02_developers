import os
import time

def interactive_calculator():                                 # Função para realizar o cálculo
    while True: 
        # Solicitando entrada ao usuário
        number1 = input('Digite um número: ')
        number2 = input('Digite outro número: ')
        operation = input('Digite um operador: \n | + | - | * | / |: ')

        numbers_validateds = None                              # Indica se ambas as entradas do usuário são válidas
        num1 = 0                                               # Inicializando a variável para o primeiro número
        num2 = 0                                               # Inicializando a variável para o segundo número

        try:
            num1 = float(number1)                              # Tentando converter a entrada do usuário para float
            num2 = float(number2)
            numbers_validateds = True
        except ValueError:
            numbers_validateds = None                          # Se houver um ValueError (entrada inválida), num_validos permanece como None

        if numbers_validateds is None:
            print('Um ou ambos os números são inválidos.')
            continue                                           # Volta para o início do loop se a entrada não for válida

        operators = '+-*/'

        if operation not in operators:
            print('Operador inválido.')
            continue                                           # Volta para o início do loop se o operador não for válido

        if len(operation) > 1:
            print('Digite apenas um operador.')
            continue                                           # Volta para o início do loop se o usuário inserir mais de um operador

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '/':
            print(num1 / num2)
        elif operation == '*':
            print(num1 * num2)
        else:
            print('Entrada inválida. Tente novamente.')

        exit_calculation = input('Deseja sair? Digite [Sim] para Sair ou pressione outra tecla para continuar: ').lower().startswith('sim' and 's')

        if exit_calculation:
            print('Encerrando...')
            time.sleep(0.5)                                   # Aguarda 0.5 segundos para exibir a mensagem de encerramento
            os.system('cls')                                  # Limpa a tela do console (Windows)
            return True                                       # Retorna True para indicar que o usuário quer sair

# Chama a função
interactive_calculator()

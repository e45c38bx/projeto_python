# Faça um programa que receba 2 valores, faça a divisão entre eles.
# Se a divisão não for inteira, o programa deverá arredondar o 
# resultado para cima e para baixo. Faça a validação para divisão por 0.

import math
import os

os.system('cls')

numero_01 = float(input('Digite o primeiro número (dividendo): '))
numero_02 = float(input('Digite o segundo número(divisor): '))

if numero_02 == 0:
    print('Erro, não é possível dividir por 0')

    resultado = numero_01 / numero_02

    # Arredondando para cima e para baixo
    resultado_arredondado_cima = math.ceil(resultado)
    resultado_arredondado_baixo = math.floor(resultado)

    print(f'O resultado da divisão é: {resultado}')
    print(f'Arredondado para cima: {resultado_arredondado_cima}')
    print(f'Arredondado para baixo: {resultado_arredondado_baixo}')

    print('Por favor, digite números válidos')





# Faça um programa que receba um valor e mostre sua raiz quadrada. 
# Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos, avisando ao usuário que o 
# resultado será um número complexo.

import math
import os

os.system('cls')

valor = float(input('Entre com um número: '))

if valor < 0:
    print('O resultado será um número complexo')

    raiz_quadrada = math.sqrt(valor)
    print(f'A raiz quadrada de {valor} é {raiz_quadrada}')

    escolha = input('Deseja arredondar para (c)ima ou para (b)aixo? (c/b):')

    if escolha == 'c':
        raiz_arredondada = math.ceil(raiz_quadrada) # Arredonda para cima
        print('A raiz quadrada arredondada para cima é: {raiz_arredondada}')
    elif escolha == 'b':
        raiz_arredondada = math.floor(raiz_quadrada) # Arredonda para baixo
        print('A raiz arredondada para baixo é: {raiz_arredondada}')
    else:
        print('Opção inváida! Escolha c para cima ou b para baixo.')

        print('Por favor, digite um número válido')





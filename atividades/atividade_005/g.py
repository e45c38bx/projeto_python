# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os

os.system('cls')

print('-'*70)
print('CALCULANDO NÚMEROS PRIMOS')
print('='*70)

inicio = int(input('Entre com o inicio: '))
fim = int(input('Entre com o fim: '))

for i in range(inicio, fim):

    divisor = 0
    for c in range(1, i + 1):
        if i % c == 0:

            divisor += 1
            soma =+ i

    if divisor == 2:
            
            print(f'O número {c} é um número primo')

            print()
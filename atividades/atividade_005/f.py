# Faça um programa que imprima os números primos entre 0 e 100.

import os

os.system('cls')

print('-'*70)
print('NÚMEROS PRIMOS')
print('='*70)

numero = 0

for i in range(1, 101):
    if i > 1:
        if i % 1 == 0:
            print(f'O número {numero} é primo')
            if i < 1:
                print(f'O número {numero} não é primo')
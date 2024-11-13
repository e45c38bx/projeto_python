# Faça um programa que imprima os números pares entre 0 e 100.

import os

os.system('cls')

print('-'*70)
print('IMPRIMINDO NÚMEROS PARES')
print('='*70)

for i in range(1, 100):
    if i % 2 == 0:
        print(i)
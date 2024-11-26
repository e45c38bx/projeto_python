# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os

os.system('cls')

lista = [10, 20, 30, 40, 50]
soma = 0

for c in range(0,5):

    soma += lista[c]
print(f'A soma é {soma}')
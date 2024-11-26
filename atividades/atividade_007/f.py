# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os

os.system('cls')

nomes = ["Ana", "João", "Liv", "Lana", "Amanda"]

indice = [0,6]

if indice in nomes:
    indice = nomes.index()
    print(f'O índice é: {indice}')
# Faça um programa que receba um nome e imprima esse nome em maiúsculo e minúsculo

import os

os.system('cls')

nome = str(input('Entre com o nome: '))

nome_maiusculo = nome.upper()

nome_minusculo = nome.lower()

print(f'O {nome} em maiúsculo é: {nome_maiusculo}')
print(f'O {nome} em minúsculo é: {nome_minusculo}')
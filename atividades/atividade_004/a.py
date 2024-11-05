# Faça um programa que solicite separadamente o nome, o nome do meio e 
# o sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os

os.system('cls')

nome = str(input('Entre com o nome: '))
nome_do_meio = str(input('Entre com nome do meio: '))
sobrenome = str(input('Entre com sobrenome: '))

print(f'O nome completo é: {nome} {nome_do_meio} {sobrenome}')

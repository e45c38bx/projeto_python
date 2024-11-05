# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os

os.system('cls')

nome = input('nome: ')

substituicao = nome.replace('Silva', 'Oliveira')
print(f'Frase original: {nome}')
print(f'Frase nova: {substituicao}')




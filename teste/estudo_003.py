# Faça um programa que receba uma frase e indique a posição do primeiro e do último caractere e 
# que conte os caracteres também

import os

os.system('cls')

frase = str(input('Entre com a frase: '))

indicar_posicao_primeiro = frase.find('o') +1

indicar_posicao_ultimo = frase.rfind('o') +1

contar_caracteres = len(frase)

print(f'Foi indicado a primeira posição {indicar_posicao_primeiro}')
print(f'Foi indicado a última posição {indicar_posicao_ultimo}')
print(f'Foi contado os caracteres da frase {contar_caracteres}')
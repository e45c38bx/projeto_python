# Faça um programa que peça ao usuário um nome completo e retire dele os espaços em branco
# e conte quantas letras "a" tem nele.

import os

os.system('cls')

nome_completo = str(input('Entre com o nome completo: '))

remover_espaços_em_branco = nome_completo.strip()

contar_a = nome_completo.count('a')

print(f'Foi removido do {nome_completo} os espaços em branco {remover_espaços_em_branco}')
print(f'Foram contadas {contar_a} as letras a do {nome_completo}')
# Faça um programa que leia o nome de um aluno e mostre quantas vezes 
# a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os

os.system('cls')

nome = str(input('Entre com um nome: ')).lower()

# Contar quantas vezes a letra 'o' aparece
quantidade_o = nome.count('o')

# Encontrar a posição da primeira e última ocorrência de 'o'
if quantidade_o > 0:
    primeira_posicao = nome.find('o') + 1  # A função find retorna o índice da primeira ocorrência
    ultima_posicao = nome.rfind('o') + 1    # A função rfind retorna o índice da última ocorrência
    print(f"A letra 'o' aparece {quantidade_o} vez(es).")
    print(f"A primeira ocorrência de 'o' está na posição {primeira_posicao}.")
    print(f"A última ocorrência de 'o' está na posição {ultima_posicao}.")
else:
    print("A letra 'o' não foi encontrada no nome.")


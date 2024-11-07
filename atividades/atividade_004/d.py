# Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de 
# caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os

os.system('cls')

frase = 'Eu amo o Justin Bieber'

# Tornar a frase em minúscula:
minuscula = frase.lower()

# Tornar a frase em maiúscula:
maiuscula = frase.upper()

# Contar caracteres:
caracteres = frase.count('a')

# Contar quantidade de letras que tem na segunda palavra da frase
contagem_letras = 'amo'

jb = len(contagem_letras)

print(f'Frase em minúscula: {minuscula}')
print(f'Frase em maiúsculo: {maiuscula}')
print(f'Contar caracteres: {caracteres}')
print(f'Quantidade de letras que tem na segunda palavra da frase: {jb}')


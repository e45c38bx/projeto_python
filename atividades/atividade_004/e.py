# Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.

import os

os.system('cls')

frase = str(input('Entre com uma frase: '))

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

print(f'A vogal (a) é usada {a}')
print(f'A vogal (e) é usada {e}')
print(f'A vogal (i) é usada {i}')
print(f'A vogal (o) é usada {o}')
print(f'A vogal (u) é usada {u}')




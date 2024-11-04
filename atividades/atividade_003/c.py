# Faça um programa que receba as informações de base e expoente. Calcule a potência.

import math
import os

os.system('cls')

base = float(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))

resultado = base ** expoente 

print(f'{base} elevado a {expoente} é igual a {resultado}')

print('Por favor, digite valores válidos')
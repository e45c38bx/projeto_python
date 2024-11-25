# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

import os

os.system('cls')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# fatiamento intervalo 1 até 9
lista_1 = lista_numeros[0:9]
print(lista_1)

# fatiamento intervalo 8 até 13
lista_2 = lista_numeros[7:13]
print(lista_2)

# invertendo a lista
lista_numeros.reverse()
print(f'Lista invertida {lista_numeros}')

# produto do intervalo
produto_1 = lista_numeros [5] * lista_numeros [11]
produto_2 = lista_numeros [6] * lista_numeros [12]

# lista de pares
for lista_numeros in range(1, 15):
    if lista_numeros % 2 == 0:
        print(f'O número {lista_numeros} é par')
    else:
        print(f'O número {lista_numeros} é ímpar')

# lista de ímpares
for lista_numeros in range(0, 15):
    if lista_numeros % 2 != 0:
        print(f'O número {lista_numeros} é ímpar')
    else:
        print(f'O número {lista_numeros} é par')


# multiplos de 2
for i in range(0, 15):
    if i % 2 == 0:
        print(f'{i}, é multiplo de 2')
# multiplos de 3
for i in range(0, 15):
    if i % 3 == 0:
        print(f'{i}, é multiplo de 3')
# multiplos de 4
for i in range(0, 15):
    if i % 4 == 0:
        print(f'{i}, é multiplo de 4')


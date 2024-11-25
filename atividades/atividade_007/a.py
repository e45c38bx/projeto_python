# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os

os.system('cls')

print('-'*70)
print('CRIANDO LISTA')
print('='*70)

lista = [1, 2, 3, 5, 6]

for i in range(4):
    lista_nova = int(input('Entre com o numero que falta: '))

    lista.insert(3, 4)
    print(f'Lista gerada {lista}')
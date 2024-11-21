import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE DAODOS: LISTAS []')
print('='*70)

lista_mista = ['a', 'b', 3, 'Jonh', 'e', 500, 'g', 'h']

# Fatia o 1° elemento
lista_fatiada_1 = lista_mista[0]
# Fatia todos os elementos 
lista_fatiada_2 = lista_mista[0:]
# Fatia os elementos do índice 0 até o índice 6
lista_fatiada_3 = lista_mista[0:6]
# Fatia os elementos do índice 0 até o índice 6 de 2 em 2
lista_fatiada_4 = lista_mista[0:6:2]
# Fatia os elementos da direita para a esquerda 
lista_fatiada_5 = lista_mista[::-1]

print(f'Fatiando uma lista: {lista_fatiada_1}\n')
print(f'Fatiando uma lista: {lista_fatiada_2}\n')
print(f'Fatiando uma lista: {lista_fatiada_3}\n')
print(f'Fatiando uma lista: {lista_fatiada_4}\n')
print(f'Fatiando uma lista: {lista_fatiada_5}\n')

print('-'*70)
print('Fim do programa!')
print('='*70)

import os

os.system('cls')

print('-'*70)
print('Funções string')
print('='*70)

frase1 = 'Olá, mundo!'
quantidade_caracteres = len(frase1) # Conta os caracteres
print(f'A frase {frase1} /ncontém {quantidade_caracteres} caracteres')
print('.'*70)

minusculas = frase1.lower()
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

capitalizada = frase1.capitalize() # Frase capitalizada
print(f'Frase original: {frase1}')
print(f'Frase capitalizada: {capitalizada}')
print('.'*70)

frase2 = 'Olá, mundo'
sem_espacos = frase2.strip() # Retirar espaços, antes e depois 
print(f'Frase original: {frase1}')
print(f'Frase nova: {sem_espacos}')
print('.'*70)

substituicao = frase1.replace('Mundo, Python') # Troca palavra 
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print('.'*70)

lista = frase1.split(',') # Separa as palavras de uma str em uma lista
print(f'Frase original: {frase1}')
print(f'Frase nova: {lista}')
print('.'*70)

lista = ['Olá', 'mundo']
juncao = "-".jonh (lista) # Transforma uma lista em uma string com reparador 
print(f'Frase original: {lista}')
print(f'Frase nova {juncao}')
print('.'*70)





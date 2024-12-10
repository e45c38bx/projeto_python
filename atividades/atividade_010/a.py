import os
os.system('cls')

print('-'*70)
print('CRIANDO DICIONÁRIO')
print('='*70)

meu_dicionario = {}

for c in range(1, 5):

    chave = str(input('Insira sua chave: '))
    valor = (input('Insira seu valor: '))

    meu_dicionario[chave] = valor
print(meu_dicionario)


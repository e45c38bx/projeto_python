# A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos
# bissextos para auxiliar usuários na identificação desses anos de forma rápida
# e precisa. Eles precisam de um programa que permita aos usuários inserir um ano e, 
# em seguida, determine se esse ano é bissexto ou não, de acordo com as regras
# estabelecidas pelo calendário gregoriano. Além disso, é necessário realizar a
# validação de entrada de dados para garantir que o ano inserido pelo usuário 
# seja um valor válido, ou seja, um número inteiro positivo.

import os

os.system('cls')

print('-'*70)
print('ANO BISSEXTO')
print('='*70)

ano = int(input('Entre com o ano:' ))

if ano <= 0:
    print(f'Ano inválido')

if ano % 100 != 0 and ano % 4 == 0 or ano % 400:
    print(f'Ano bissexto')
else:
    print(f'Ano comum!')


# A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para 
# auxiliar usuários na identificação desses anos de forma rápida e precisa. Eles precisam de um
# programa que permita aos usuários inserir um ano e, em seguida, determine se esse ano é bissexto 
# ou não, de acordo com as regras estabelecidas pelo calendário gregoriano. Além disso, é necessário
# realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário seja um 
# valor válido, ou seja, um número inteiro positivo.

import os

os.system('cls')

print('-'*70)
print('ANO BISSEXTO')
print('='*70)

valor = int(input('Entre com valor: '))


# Processamento 01
# if ano < 1582 :
#     print('Não está dentro do período do calendário gregoriano')
# elif (ano % 100) == 0 and (ano % 400) == 0 :
#     resultado = 'ano bissexto'
# elif (ano % 100) == 0 :
#     resultado = 'ano comum'
# elif (ano % 4) == 0 :
#     resultado = 'ano bissexto'
# else:
#     resultado = 'ano comum'


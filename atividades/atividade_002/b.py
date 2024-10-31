#  A empresa "DataMax" está desenvolvendo um novo software de análise estatística e 
# precisa de uma funcionalidade que permita aos usuários inserir três números e, em 
# seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números
#  são todos iguais. Essa funcionalidade é crucial para os analistas de dados da 
# "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente 
# identificar as características básicas desses conjuntos, como a presença de outliers 
# ou a uniformidade dos números.

import os

os.system('cls')

print('-'*70)
print('Desvendando números')
print('='*70)

a = int(input('Entre com a: '))
b = int(input('Entre com b: '))
c = int(input('Entre com c: '))

if (a > b and a > c):
    print(f'{a} é o maior valor')

if (b > c and b > a):
    print(f'{b} é o maior valor')

if (a < b and a < c):
    print(f'{a} é o menor valor')

if (b < a and b < c):
    print(f'{b} é o menor valor')

if (a == b and b == c):
    print('Todos os valores são iguais')


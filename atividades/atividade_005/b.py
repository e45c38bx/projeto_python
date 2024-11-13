# Evolua o programa anterior para um código que pergunte ao 
# usuário qual o intervalo que ele deseja ver  impresso.

import os

os.system('cls')

print('-'*70)
print('EVOLUINDO PROGRAMA E IMPRIMINDO')
print('='*70)

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))

for i in range(inicio, fim):
    print(i)

    
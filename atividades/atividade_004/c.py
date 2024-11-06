# Faça um programa que leia o nome de uma pessoa e verifique 
# se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os

os.system('cls')

nome = str(input('Entre com um nome: '))

if 'Oliveira' in nome:
    print('Retorna true, se estiver presente no nome')
else:
    print('Retorna false, se não estiver presente no nome')




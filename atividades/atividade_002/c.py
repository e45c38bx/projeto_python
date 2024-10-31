# A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar
# a promover a segurança nas estradas. Eles precisam de um programa que permita aos usuários 
# inserir a velocidade de um carro e, em seguida, exibir na tela uma mensagem adequada com base 
# na velocidade fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o 
# limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites legais e, assim,
# reduzir o risco de acidentes.

import os

os.system('cls')

print('-'*70)
print('MONITORAMENTO DE VELOCIDADE')
print('='*70)

# Entrada
valor_01 = int(input('Entre com a velocidade: '))

if('valor_01 > 60km/h'):
    print(f'Limite de velocidade ultrapassado')
else:
    print('Velocidade normal')
    print('-'*70)
    




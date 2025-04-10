# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança
#  nas estradas. Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e,
#  em seguida, exibir na tela uma mensagem adequada com base na velocidade fornecida. O objetivo principal
#  é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a dirigir
#  dentro dos limites legais e, assim, reduzir o risco de acidentes.

import os
os.system('cls')

velocidade_carro = int(input('Entre com a velocidade: '))

if velocidade_carro > 60:
    print('Ultrapassou o limite')
else:
    print('Não ultrapassou o limite')
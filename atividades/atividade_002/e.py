# A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de
# ônibus com base na distância da viagem. Eles precisam de um programa que solicite ao 
# usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com
# as políticas da empresa. Segundo essas políticas, viagens de até 200 km têm um custo de
# R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.

import os

os.system('cls')

print('-'*70)
print('CALCULANDO PASSAGENS')
print('='*70)

valor = float(input('Entre com o valor: '))
if valor <= 200:
    preco = valor * 0.70
    print('-'*70)
    print(f'o preço da viagem é igual a: {preco} ')

else:
    valor >= 200
preco = valor * 0.40
print('-'*70)
print(f'o preço da viagem é igual a: {preco}')

    


# imports
import os

os.system(' cls ')

#Implemente um programa que receba dois números e realize a divisão, formatando o resultado com quatro casas decimais.
numero_01 = (int(input('Entre com o primeiro número:' )))
numero_02 = (int(input('Entre com o segundo número:' )))

# Processamento
quociente = numero_01 / numero_02 

# Saída 
print('-'*70)
print('RESULTADOS')
print('='*70)
print(f'A divisão de {numero_01} e {numero_02} é: ')



import os 
os.system('cls')

numero = float(input('Digite um número:'))
resposta = ''

# Condicional
if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

print('='*70)
print(resposta)
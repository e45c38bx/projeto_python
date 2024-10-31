# Você está desenvolvendo um programa para determinar se três segmentos 
# podem formar um triângulo. Para isso, o programa precisa receber as 
# medidas dos três segmentos e compará-las entre si. A resposta resultante 
# dessa comparação deve indicar se os segmentos fornecidos podem formar 
# um triângulo ou não.

import os

os.system('cls')

print('-'*70)
print('COMPARANDO TRIÂNGULOS')
print('='*70)

# Entrada
a = float(input('Digite a medida do segmento: '))
b = float(input('Digite a medida do segmento: '))
c = float(input('Digite a medida do segmento: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Os segmentos devem ser maiores que zero')

if (a, b, c):
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")



#  A empresa "TechSolutions" contratou você para 
# desenvolver um programa em Python que irá automatizar 
# uma parte do seu sistema de processamento de dados. 
# Eles precisam de um programa que solicite ao usuário a 
# entrada de um número inteiro e, em seguida, verifique se 
# esse número é par ou ímpar. Essa funcionalidade é essencial 
# para o sistema deles, pois eles processam grandes conjuntos 
# de dados e precisam classificar os números de forma eficiente 
# para realizar cálculos específicos em cada tipo de número.

import os

os.system('cls')

print('-'*70)
print('Verificação de números')
print('='*70)

# Entrada
valor = int(input('Entre com um valor:'))

# Condicional
if valor % 2 == 0:
    resposta = f'o numero {valor} é par' 
else: 
    resposta = f'o numero {valor} é ímpar'

# Saída
print('-'*70)
print('Fim do programa/n')

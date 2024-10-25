# imports
import os

# limpar o terminal
os.system (' cls ')

print('-'*70)
print('OPERADORES ARITMÉTRICOS')
print('=')

# entrada de dados
print('.....SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1° parcela: '))
parcela_2 = float(input('Entre com a 2° parcela: '))

print()
print('.......SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Entre com o minuendo:  '))
subtraendo = float(input('Entre com a subtraendo:  '))

print()
print('........PRODUTO')
print('-'*70)
multiplicador = float(input('Entre com o multiplicador: '))
multiplicando = float(input('Entre com o multiplicando: '))

print()
print('.....DIVISÃO')
print('-'*70)
dividendo = float(input('entre com o dividendo:' ))
divisor = float(input('Entre com o divisor:' ))

print()
print('........RAIZ QUADRADA')
print('-'*70)
valor_quadrado = float(input('Entre com o valor da raiz quadrada: '))

print()
print('........... RAIZ CÚBICA')
print('-'*70)
valor_cubico = float(input('Entre com o valor da raiz cubica: '))

# Processamento 
soma = parcela_1 + parcela_2
diferença = minuendo - subtraendo
produto = multiplicando + multiplicador
quociente = dividendo / divisor
valor_1 = valor_quadrado **(1/2)
valor_2 = valor_cubico **(1/3)

# Saída 
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferença}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} + {divisor} é: {quociente}')
print(f'O valor de {valor_quadrado} é: {valor_1}')
print(f'O valor de {valor_cubico} é: {valor_2}')
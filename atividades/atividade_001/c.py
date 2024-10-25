# imports
import os

os.system(' cls ')

# Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas.
nota_01 = int(input('Receba a nota do usuário: '))
nota_02 = int(input('Receba a nota do usuário: '))
nota_03 = int(input('Receba a nota do usuário: '))
nota_04 = int(input('Receba a nota do usuário: '))

# Calcule a média dessas notas:
soma = nota_01 + nota_02 + nota_03 + nota_04 / 4

# Saída
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {nota_01} + {nota_02} + {nota_03} + {nota_04}: ')
print(f'A divisão de {soma} / {4}: ')





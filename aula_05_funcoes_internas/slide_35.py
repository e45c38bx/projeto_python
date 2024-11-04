import math
import os

os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('='*50)
print()

# Entrada de dados
numero_decimal = float(input('Entre com número decimal: '))

# Processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# Saída
print('-'*50)
print(f'O número {numero_decimal} arredondado para cima é {arredondar_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é {arredondar_para_baixo}')
print('-'*50)
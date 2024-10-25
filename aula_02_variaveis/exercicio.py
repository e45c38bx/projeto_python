# imports
# biblioteca para interagir o OS
import os

# limpar o terminal
os.system ( ' cls ')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('=')

# Entrada
rg = int(input('entre com rg: '))
peso = float(input('entre com peso: '))
nome = str(input('entre com nome: '))
brasileiro = bool(input('entre com verdadeiro ou falso: '))


# Saída interpolada
print(f'{rg}, você possuí número... {rg}!')
print(f'peso.......................{peso}')
print(f'nome.......................{nome}')
print(f'brasileiro...........{brasileiro}')

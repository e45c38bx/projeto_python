import os
os.system('cls')

numeros = []

numero_para_contar = int(input('Digite o número que deseja contar: '))

contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista')
else:
    print(f'O número {numero_para_contar} não aparece na lista')
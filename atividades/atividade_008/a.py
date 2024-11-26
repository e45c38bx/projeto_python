# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os

os.system('cls')

notas_invertida = []
lista = []
soma = 0
notas = input('Digite "s" para sair: ')
while(notas != 0 and notas != "s"):

    lista.append(notas)

# Calculando a soma das notas 
    notas = int(notas)
    soma += notas
    print(soma)

    print('Digite "s" para sair: ')
    notas = input('Digite uma nota: ').strip().lower()
    
print(f'Quantidade de notas {len(lista)}')

# Exibe as notas na ordem que foram informadas
lista_quantidade = int(len(lista))

# Calculando a média das notas
media = soma / lista_quantidade
print(f'A média é: {media}')

# Exibe as notas em ordem inversa, uma abaixo da outra
notas_invertida = lista[::-1]
print(notas_invertida)
for i in range(0,lista_quantidade):
    print(f'Notas invertidas {notas_invertida[i]}')





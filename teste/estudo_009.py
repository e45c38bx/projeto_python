import os

os.system('cls')

lista = [1, 2, 3, 4, 5]
valores = []
lista.sort(reverse=True)
print(lista)

print(f'Essa lista tem {len(lista)} elementos')

lista.insert(2, 0)
print(lista)

for count in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    print(f'Adiciona valores {valores} na lista {lista}')

busca_numero = int(input('digite o número que procura: '))


if busca_numero in lista:
    indice = lista.index(busca_numero)
    print(f'O valor {busca_numero} está no índice {indice}')
else:
    print(f'O valor {busca_numero} não está no índice ')



item_removido = int(input('digite o número que deseja retirar: '))

if 0<= item_removido < len(lista):

    item_removido = lista.pop(0)
print(lista)
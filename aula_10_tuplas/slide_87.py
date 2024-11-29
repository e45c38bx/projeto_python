import os

os.system('cls')

nomes = ['Ágata', 'Bia', 'Coly', 'Ísis']

for indice, nome in enumerate(nomes):
    # Cria uma tupla com o índice e o nome da pessoa atual
    minha_tupla = (indice, nome)
    # A variável minha_tupla é usada para acessar o 
    # índice e o armazenamento da tupla.
    # Mas posso acessar diretamente os elementos 'índice' e 'nome'.
    print(f"O nome '{minha_tupla[1]}', posição {minha_tupla[0]} da lista")
    print(f"O nome '{nome}', posição {indice} da lista")
    print('-'*70)
import os

os.system('cls')

# Solicite ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte uma lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário o número que deseja encontrar na lista
    busca_numero = int(input('Digite o número que deseja encontrar: '))

    # Tenta encontrar o índice do número fornecido
    if busca_numero in numeros:
        indice = numeros.index(busca_numero)
        print(f'O número {busca_numero} está no índice {indice}')
    else:
        print(f'O número {busca_numero} não foi encontrado na lista')

        # Exibe a lista fornecida para referência
        print(f'Lista fornecida: {numeros}')
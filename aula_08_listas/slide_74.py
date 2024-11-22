import os

os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em umas lista de strings
numeros_str = entrada.split

# Converte umas lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário se deseja limpar a lista
escolha = input('Deseja limapr a lista? (s/n): ').strip().lower()

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

# Verifica a escolha do usuário e limpa a lista se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')
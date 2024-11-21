import os

os.system('cls')

# Inicializa a lista vazia 
lista_numeros = [100, 200]

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros = entrada.split()

# Cria uma lista para armazenar números pares
pares = []

# Itera sobre os números inseridos
for numero in numeros:
    # Converte a string para inteiros
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par á lista de pares
        pares.append(numero_aux)
print('-'*70)
print(f'Lista gerada: {pares}')
print('-'*70)

# Usa extend para adicionar todos os números pares á lista inicial
lista_numeros.extend(pares)

# Exibe a linha resultante
print(f'Números pares adicionados á lista:{lista_numeros}')
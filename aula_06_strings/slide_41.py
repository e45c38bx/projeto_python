import os

os.system('cls')

print('-'*70)
print('Fatiamento de strings')
print('='*70)

frase = 'Strings em Python!'

# Exibindo a string original 
print(f'String original: {frase}')

# Fatiamento: acessando partes específicas da string
# Primeiros cinco caracteres
primeiros_cinco = frase[:5]
print(f'Primeiros cinco caracteres: {primeiros_cinco}')

# Últimos dez caracteres
ultimos_dez = frase[-10:]
print(f'Últimos dez caracteres: {ultimos_dez}')

# A cada dois caracteres
a_cada_dois = frase[::2]
print(f'A cada dois caracteres: {a_cada_dois}')

# Invertendo a string 
invertida = frase[::-1]
print(f'String invertida: {invertida}')
print()
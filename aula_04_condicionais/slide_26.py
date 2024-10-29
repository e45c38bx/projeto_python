import os

os.system('cls')


# Declaração
a = 10
b = 5
c = 'Jonh'

print('-'*70)
print('Condicionais: Operadores Lógicos')
print('='*70)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else: 
    print('Falso: Bloco executado')

print('.'*70)

# E (and) Falso
print('E (and) Falso')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco Executado') 
else: 
    print('Falso: Bloco Executado')

print('.'*70)

# OU or VERDADEIRO
print('E (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco Executado')
else:
    print('Falso: Bloco Executado')

print('.'*70)

# E (and) Falso
print('E (and) Falso')
print('OU (or) FALSO')
if (a > 5 or c == 'Jane'):
    print('Verdadeiro: Bloco Executado')
else:
    print('Falso: Bloco Executado')
print('.'*70)
print()



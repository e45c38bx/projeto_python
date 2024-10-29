import os

os.system('cls')

# Declarações
a = 10
b = 5 
resposta = ' '

print('-'*70)
print('Estudo de condicionais(simples)')
print('='*70)

# Condicionais
if a > b:
     resposta = f'{a} é maior que {b}' 
else:
     resposta = f'{a} não é maior que {b}'

# Saída
print('-'*70)     
print(resposta)

# Declarações 
a = 5
b = 5

print('-'*70)
print('Estudo de condicional (aninhada)')
print('='*70)

if a > b:
      resposta = f'{a} é maior que {b}'
elif a < b:
     resposta = f'{a} é menor que {b}'
else:
     resposta = f'Os valores são iguais {a} = {b}'

# Saída
print('-'*70)
print(resposta)
print('='*70)
print()




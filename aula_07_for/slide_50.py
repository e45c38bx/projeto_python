import os

os.system('cls')

print('-'*50)
print('ESTRUTURA DE CONTROLE SOMATÓRIO')
print('='*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input('Digite o {var_iteradora +1}º número: '))

    # Cálculo
    soma+= numero  # Mesma coisa: soma = soma + numero

    print('-'*50)
    print(f'A soma dos números é: {soma}')
    print('='*50)
    print()

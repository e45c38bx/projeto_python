import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE COMANDO BREAK')
print('='*70)

print()

for c in range(0, 10):

    print(f'Valor {c}')

    # Condição para terminar a contagem
    if (c == 5):
        print(f'Contagem interropida no {c}')
        break

print('-'*70)
print('Fim do programa!')
print('='*70)
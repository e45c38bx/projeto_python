import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('='*70)

while(True):

    # lower garante o tratamento para entrada de 's' ou 's'
    nome = str(input('Digite um nome [s - Sair]:')).lower()

    if(nome != 's'):
        print('Continue digitando...')
    else:
        print('-'*70)
        print('Você digitou "s" para sair!')

        # Interrompe o laço 
        break

    print('-'*70)
    print()
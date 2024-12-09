import os
os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\nMenu de opções')
    print('1. Adicionar um par chave-valor')
    print('2. Remove um item usando pop()')
    print('3. Remover o último item usando popitem')
    print('4. Mostrar o dicionario atual')
    print('5. Sair')
    print('-'*70)

    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adiciona um par chave-valor ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado')

    elif opcao == '2':
        # Remove um item específico usando pop()
        if meu_dicionario:
            chave = input('Digite a chave do item que deseja remover: ')
            valor_removido = meu_dicionario.pop(chave, 'chave não encontrada')
            print(f'Item removido: {chave}: {valor_removido}')
        else:
            print('O dicionario esta vazio. Adicione iten primeiro')

    elif opcao == '3':
        # Removi o último item usando popitem()
        if meu_dicionario:
            chave, valor = meu_dicionario.popitem()
            print(f'Ultimo item removido: {chave}: {valor}')
        else:
            print('O dicionario esta vazio. Adicione itens primeiro')

    elif opcao == '4':
        # Mostra o dicionario atual
        if meu_dicionario:
            print('Dicionario atual', meu_dicionario)
        else:
            print('O dicionario esta vazio')

    elif opcao == '5':
        print('Saindo do programa')
        break

    else:
        print('Opção inválida. Tente novamente')
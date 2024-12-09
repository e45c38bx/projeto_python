import os


elementos = {}
periodica = []

while True:
    os.system('cls')

    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos ')
    print('3. Atualizar um Elemento')
    print('4. Remover um elemento')
    print('5. Sair')

    opcao = input('escolha uma opção (1-5): ')

    if opcao == '1':
        simbolo = str(input('Simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input('\nElemento adicionado. Pressione enter para continuar')

    elif opcao == '2':
        print('\nElementos da tabela periodica')
        for elementos in periodica:
            for chave, valor in elementos.items():
                print(f'{chave.capitalize()}: {valor}')
                input('\nPressione enter para continuar')

    elif opcao == '3':
        simbolo = str(input('Digite o simbolo do elemento para atualizar: '))
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input('Digite o novo simbolo para' f'{simbolo} (ou deixe em branco para manter o atual)'))
                novo_nome = str(input('Digite novo nome para' f'{nome} (ou deixe em branco para manter o atual)'))

                if novo_simbolo:
                    elementos['simbolo'] = simbolo
                    if novo_nome:
                        elementos['nome'] = nome

                        encontrado = True
                        break

                    if encontrado:
                        input('\nElemento atualizado. Enter para continuar')
                    else:
                        input('\nElemento não encontrado. Enter para continuar')

    elif opcao == '4':
        simbolo = str(input('Digite o simbolo do elemento que deseja remover: '))
        encontrado = False
        for elementos in periodica:
            if elemento[simbolo] == simbolo:
                periodica.remove(elemento)
                encontrado = True
                break

            if encontrado:
                input('\nElemento removido. Enter para continuar')
            else:
                input('\nElemento não encontrado. Enter para continuar')

    elif opcao == '5':
        print('Saindo do programa')
        break
    else:
        print('Opção invalida. Enter para tentar novamente')
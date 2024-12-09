import os

agenda = {
    'Jojo': '9999-7777',
    'Dio': '8888-9999',
    'Ana': '2222-3333',
    'Lara': '3333-7777',
    'Solange': '4444-9999',
    'Wellington': '5555-6666',
    'Zezin': '1111-3333'
        }

while True:
    os.system('cls')

    print('-'*70)
    print('\nAgenda de contatos')
    for nome, telefone in agenda.items():
        print(f'{nome}: {telefone}')
        print('-'*70)

        # Primeiro teste: Verificar se 'jojo' está no dicionario
        if 'jojo' in agenda:
            print('Primeiro teste: verificando se jojo esta no dicionario')
            print('VERDADEIRO: jojo esta no dicionario')
        else:
            print('FALSO: jojo não esta no dicionario')

            print()

            # Segundo teste: verificar se jonh não esta no dicionario
            if 'jonh' not in agenda:
                print('Segundo teste: verificando se jonh não esta no dicionario')
                print('VERDADEIRO: jonh não esta no dicionario')
            else:
                print('FALSO: Jonh esta no dicionario')

                print('-'*70)
                print()
                print('\nMenu de opções')
                print('1. Adicionar um contato')
                print('2. Remover um contato')
                print('3. Verificar contato especifico')
                print('4. Mostrar agenda')
                print('5. Sair')

    opcao = input('Escolha uma opção (1-5): ')
    if opcao == '1':
        # Adiciona contato
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato {nome}: {telefone} adicionado')

     
    elif opcao == '2':
        # remover um contato
        nome = input('Digite o nome que deseja remover: ')
        if nome in agenda:
            del agenda[nome]
            print(f'Contato {nome} removido')
        else:
            print(f'Contato {nome} não encontrado na agenda')

    elif opcao == '3':
        # Verificar contato especifico
        nome = input('Digite o nome do contato que deseja verificar')
        if nome in agenda:
            print(f'Contato encontrado - {nome}: {agenda[nome]}')
        else:
            print(f'Contato {nome} não encontrado na agenda')

    elif opcao == '4':
        # Mostrar agenda atual
        print('\nAgenda de contatos')
        print(agenda)

    elif opcao == '5':
        print('Saindo do programa')
        break

    else:
        print('Opção invalida. Tente novamente')

        # Pausa para o usuario ver as mensagens antes de limpar a tela
        input('\nPressione enter para continuar')













                  
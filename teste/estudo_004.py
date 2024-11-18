import os

os.system('cls')

while True:
    numero = int(input('Entre com número inteiro: '))
    if numero % 2 != 0:
        print(f'Esse número {numero} é ímpar')
        break
    print(f'Esse número {numero} é par')

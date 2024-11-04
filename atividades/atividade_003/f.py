# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import random
import os

os.system('cls')

numero_pensado = random.randint(1,20)
tentativas = 0
print('Estou pensando em um número entre 1 a 20. Tente adivinhar!')

palpite = int(input('Digite seu palpite: '))
tentativas += 1

if palpite < 0 or palpite > 20:
    print('Por favor digite um número entre 1 e 20')
elif palpite < numero_pensado:
    print('Muito baixo! Tente novamente')
elif palpite > numero_pensado:
    print('Muito alto! Tente novamente')
else:
    print(f'Parabéns! Você acertou o número {numero_pensado} em {tentativas} tentativas')

    print('Por favor, digite um número váldo')
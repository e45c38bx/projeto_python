# Faça um programa que receba um ângulo qualquer. Em seguida, calcule o seno, 
# cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

import math
import os

os.system('cls')

angulo = float(input('Digite o ângulo em graus: '))
    # Converte o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

    # Calcula seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

    # Exibe os resultados com duas casas decimais
print(f'Seno de {angulo}°: {seno:.2f}')
print(f'Cosseno de {angulo}°: {cosseno:.2f}')
print(f'Tangente de {angulo}°: {tangente:.2f}')

   
print("Por favor, digite um valor válido para o ângulo.")


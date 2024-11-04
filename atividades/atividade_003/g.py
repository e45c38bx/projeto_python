# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau. 
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import math
import os

os.system('cls')

a = float(input('Digite valor de a: '))
b = float(input('Digite valor de b: '))
c = float(input('Digite valor de c: '))

if a == 0:
    print('O valor de a não pode ser igual a zero em uma equação de 2 grau')

    delta = b**2 - 4*a*c
    
    if delta < 0:
        print('Não há raízes reais. O discriminante é negativo')
    elif delta == 0:
        x = - b / (2*a)
        print(f'A raiz dupla é: x = {x:.2f}')
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*b)
        print(f'As raízes são x1 = {x1:.2f} e x2 = {x2:.2f}')

        print('Por favor, digite valores numéricos válidos')

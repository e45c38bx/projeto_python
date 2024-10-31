# A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes 
# de equações quadráticas para auxiliar engenheiros e cientistas em suas 
# análises e projetos. Eles precisam de um programa que calcule as raízes 
# da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, 
# utilizando apenas os conceitos e operações básicas aprendidos até o momento.
# Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser
# capaz de calcular essas raízes de forma precisa, seguindo os princípios 
# matemáticos fundamentais.

import os

os.system('cls')

print('-'*70)
print('CALCULANDO RAÍZES DE EQUAÇÕES QUADRÁTICAS')
print('='*70)

# Coeficientes da equação quadrática
a = 1
b = -6
c = 5

# Calculando o discriminante (b² - 4ac)
discriminante = b**2 - 4*a*c

# Verificando se o discriminante é não negativo
if discriminante >= 0:
    # Calculando as raízes
    raiz1 = (b * -1 + discriminante**0.5) / (2 * a)
    raiz2 = (b * -1 - discriminante**0.5) / (2 * a)

    # Imprimindo as raízes
    print(f"As raízes da equação são: x' = {raiz1} e x'' = {raiz2}")
else:
    print("A equação não possui raízes reais.")

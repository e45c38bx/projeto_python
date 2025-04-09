import os
os.system('cls')

nota_1 = float(input('Entre com a nota 1:'))
nota_2 = float(input('Entre com  a nota 2: '))
nota_3 = float(input('Entre com a nota 3: '))
nota_4 = float(input('Entre com a nota 4: '))

# Calculando a média:
calculando_media = nota_1 + nota_2 + nota_3 + nota_4 / 4

print(f"A soma das notas é: {calculando_media}")

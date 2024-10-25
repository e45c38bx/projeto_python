# imports
import os


os.system(' cls ')

# Solicita três valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Calcula a soma e a multiplicação
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# Exibe os resultados
print(f"A soma dos valores é: {soma}")
print(f"A multiplicação dos valores é: {multiplicacao}")


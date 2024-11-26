# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os

os.system('cls')

notas = [] 
media = 0
soma = 0


for i in range(1, 5):
    nota = int(input("Digite as notas de 4 alunos:"))
    notas.append(nota)
    soma += nota

media = soma /len(notas)
print(f'A média é: {media}')

                

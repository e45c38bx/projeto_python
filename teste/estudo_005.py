import os

os.system('cls')

contador = int(input('Digite o número de candidatos: '))
aprovados = 0 
reprovados = 0
media = 0
while contador > 0:
    nome = str(input('Entre com o nome do candidato: '))
    nota = int(input('Digite a pontuação do candidato: '))
    if nota > 80:
        print('O candidato foi aprovado!')
        aprovados += 1
    else:
        print('Ocandidato foi reprovado!')
        reprovados += 1
        contador -= 1
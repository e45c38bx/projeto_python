import os
os.system('cls')

# Trabalho sobre a estrutura de dados set
# Senac Minas Gerais/Juiz de Fora
# Aluno: Ana Lara Campos
# Turma: 0152
# Ano: 2024

print('-'*70)
print('ESCOLHENDO MÚSICAS')
print('='*70)

# Biblioteca de músicas
biblioteca = {
    1: {"título": "Bohemian Rhapsody", "artista": "Queen"},
    2: {"título": "Merdas acontecem", "artista": "lilgiela33"},
    3: {"título": "white tee", "artista": "Lil peep"},
    4: {"título": "Change", "artista": "Deftones"},
    5: {"título": "Thriller", "artista": "Michael Jackson"}
}

escolha_sua_faixa = int(input('Escolha sua faixa entre 1 e 5: '))
print(f'Sua faixa escolhida {escolha_sua_faixa}')
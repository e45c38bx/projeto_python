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
    2: {"título": "Imagine", "artista": "John Lennon"},
    3: {"título": "Hotel California", "artista": "Eagles"},
    4: {"título": "Shape of You", "artista": "Ed Sheeran"},
    5: {"título": "Thriller", "artista": "Michael Jackson"}
}

    exibir_biblioteca():
    """Exibe a lista de músicas disponíveis."""
    print("\nMúsicas disponíveis:")
    for chave, musica in biblioteca.items():
        print(f"{chave}. {musica['título']} - {musica['artista']}")

def tocar_musica(opcao):
    """Simula a reprodução da música."""
    musica = biblioteca.get(opcao)
    if musica:
        print(f"\n Tocando agora: {musica['título']} - {musica['artista']} 🎵")
    else:
        print("\nOpção inválida! Por favor, escolha uma música válida.")

def main():
    while True:
        exibir_biblioteca()
        print("\nDigite o número da música que deseja ouvir (ou 0 para sair):")
        try:
            escolha = int(input("Escolha: "))
            if escolha == 0:
                print("\nObrigado por usar a biblioteca de música. Até logo!")
                break
            tocar_musica(escolha)
        except ValueError:
            print("\nPor favor, insira um número válido.")


# imports
from datetime import datetime

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a idade
print(f"Sua idade atual é: {idade} anos.")

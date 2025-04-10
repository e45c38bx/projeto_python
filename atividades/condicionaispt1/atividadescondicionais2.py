 # B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos
 #  usuários inserir três números e, em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números 
 # são todos iguais. Essa funcionalidade é crucial para os analistas de dados da "DataMax" que trabalham com conjuntos 
 # de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, como a presença de 
 # outliers ou a uniformidade dos números.

import os
os.system('cls')

# Entrada
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceriro_numero = int(input('Digite o terceiro número: '))
resposta = ''

maior_numero = 0
menor_numero = 0
print()

# igualdade
if primeiro_numero == segundo_numero == terceriro_numero:
    print('Todos os números são iguais',primeiro_numero)
   
else:
   maior_numero = primeiro_numero 
   menor_numero = primeiro_numero
print()

# maior número
if segundo_numero > maior_numero:
    maior_numero = segundo_numero
if terceriro_numero > maior_numero:
    maior_numero = terceriro_numero

# menor número
if segundo_numero < menor_numero:
    menor_numero = segundo_numero
if terceriro_numero < menor_numero:
    menor_numero = terceriro_numero

print('O maior número é:', maior_numero)
print('O menor número é:', menor_numero)
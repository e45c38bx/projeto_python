# D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários
#  com base em critérios específicos. Eles precisam de um programa que receba como entrada o salário atual de
#  um funcionário e, em seguida, calcule o novo salário com base em determinadas condições. Essas condições
#  incluem um aumento de 5% caso o salário atual seja superior a R$1500,00, e um aumento de 10% caso o
#  salário atual seja inferior a R$1000,00. Além disso, o programa deve garantir que o salário informado
#  não seja igual a zero ou negativo, pois isso não seria válido.

import os
os.system('cls')

salario_atual = float(input('Entre com o salário atual: '))
salario_maior_que = 1.500
salario_menor_que = 1.000
porcentagem_1 = 5
porcentagem_2 = 10


if (salario_atual / salario_maior_que * 100):
    print(f'O salario maior que {salario_maior_que} é {salario_atual * porcentagem_1}')
    
elif (salario_atual / salario_menor_que * 100):
    print(f'O salário menor que {salario_menor_que} é {salario_atual * porcentagem_2}')


import os
os.system('cls')

meu_set = set(["hellokitty", "numetal", 19])

meu_set.add(3)
print('Adição', meu_set)

meu_set.remove("hellokitty")
print('Removendo', meu_set)

print(len(meu_set))

meu_set.discard(1)
print(meu_set)

meu_set.clear()
print(meu_set)

meu_set.update({"giancarlo"})
print('Atualizando', meu_set)

set1 = [1, 2, 3, 4, 5]
set2 = [6, 7, 8, 9, 10]

resultado = meu_set.union(set1, set2)
print(resultado)

resultado2 = meu_set.intersection(set1, set2)
print(resultado2)

meu_set.pop()
print(meu_set)
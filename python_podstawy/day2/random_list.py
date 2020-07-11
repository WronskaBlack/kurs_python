import random
lista = list(range(0, 1000))
print(lista)

# rozwiązanie nr. 1
# random.shuffle(lista)
# print(lista)

# rozwiązanie nr. 2
nowa_lista = []
for i in range(0, 1000):
    element = random.choice(lista)
    nowa_lista.append(element)
    lista.remove(element)
print(nowa_lista)


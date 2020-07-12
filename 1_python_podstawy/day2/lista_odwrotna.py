lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# rozwiązanie nr. 1
nowa_lista = []
for i in range(1, len(lista)+1):
    nowa_lista.append(lista[-i])
print(nowa_lista)

# rozwiązanie nr. 2
lista.reverse()
print(lista)

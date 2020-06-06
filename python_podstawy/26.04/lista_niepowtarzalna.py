lista = [1, 3, 5, 5, 4, 3, 2, 4, 3, 3, 4, 5]

# pierwsze rozwiązanie
nowa_lista = []
for i in lista:
    if i not in nowa_lista:
        nowa_lista.append(i)

print(nowa_lista)

# drugie rozwiązanie
print(list(set(lista)))

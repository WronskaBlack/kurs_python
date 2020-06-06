"""
indeks, gdzie suma po prawej = suma po lewej

return -1
"""


def ekwilibrium(lista):
    for i in range(len(lista)):
        if sum(lista[:i]) == sum(lista[i + 1:]):
            return i
    return -1


print(ekwilibrium([1, 2, 3, 100, 6]))

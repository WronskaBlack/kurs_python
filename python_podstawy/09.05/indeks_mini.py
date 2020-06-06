"""
indeks gdzie suma po lewej stronie jest najmniejsza

return ERROR
"""


def indeks_min_sumy(lista):
    suma = 1
    for i in range(0, len(lista)):
        if sum(lista[:i]) < suma:
            suma = sum(lista[:i])
            indeks = i
    return indeks


print(indeks_min_sumy([1, -92, 100, -100, 6]))

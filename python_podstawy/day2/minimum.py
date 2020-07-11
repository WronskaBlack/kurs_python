def minimum(lista):
    mini = lista[0]
    for i in lista:
        if i < mini:
            mini = i
    return mini


def maximum(lista):
    maxi = lista[0]
    for i in lista:
        if i > maxi:
            maxi = i
    return maxi


print(min([1, -678, 3, 40000, 5, 63244, -339483, 8000090, 9]))  # na skróty
print(minimum([1, -678, 3, 40000, 5, 63244, -339483, 8000090, 9]))

print(max([1, -678, 3, 40000, 5, 63244, -339483, 8000090, 9]))  # na skróty
print(maximum([1, -678, 3, 40000, 5, 63244, -339483, 8000090, 9]))

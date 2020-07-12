"""
in: 10
out: [2, 4, 6, 8, 10]
"""
n = int(input("Podaj liczbę: "))
lista = []

for i in range(2, n+1, 2):
    lista.append(i)

print(lista)

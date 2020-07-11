"""
input: 100

output: 1 2 6

Why?
1
1 * 1
1 * 2
1 * 2 * 3
1 * 2 * 3 * ... * 100

"""

n = int(input("Podaj liczbę: "))
i = 1
silnia = 1

while i <= n:
    silnia *= i
    print(silnia)
    i += 1

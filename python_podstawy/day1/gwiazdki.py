"""
in: 5
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n = int(input("Podaj liczbę: "))
i = 1

while i < n * 2:
    if i <= n:
        print("*" * i)
    else:
        print("*" * (2 * n - i))
    i += 1
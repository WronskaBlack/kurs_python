"""
input: 9
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

n = int(input("Podaj liczbę: "))
i = 1

while i <= n:
    print(str(i) * i)
    i += 1


"""
In: x

Jeśli x jest podzielne przez 3 to print "fizz"
Jeśli x jest podzielne pzez 5 to print "bizz"
Jeśli x jest podzilne przez 3 i 5 print "fizzbizz"
"""

x = int(input("Podaj liczbę: "))

if x % 3 == 0:
    print("fizz", end="")
    if x % 5 == 0:
        print("bizz")
elif x % 5 == 0:
    print("bizz")

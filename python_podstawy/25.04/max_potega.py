n = int(input("Podaj liczbę: "))
max = 32_000_000
i = 0

while n ** i < max:
    print(n ** i)
    i += 1

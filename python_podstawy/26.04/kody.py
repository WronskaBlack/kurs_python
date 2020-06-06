def code_list(code1, code2):

    x = 1000 * int(code1[:2]) + int(code1[3:])  # zamiana kodu na liczbę
    y = 1000 * int(code2[:2]) + int(code2[3:])
    lista = []

    if x > y:   # sprawdzanie który kod jest mniejszy i zamiana jeśli potrzeba
        x, y = y, x

    for i in range(x, y + 1):   # przejście przez wszystkie liczby od x do y
        a = i // 1000
        b = i - a * 1000
        lista.append(f"{a:02}-{b:03}")

    return lista


code1 = input("Podaj kod: ")
code2 = input("Podaj kod: ")

print(code_list(code1, code2))

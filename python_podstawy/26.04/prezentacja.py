# i = 0
# while True:
#     print("Hello")
#     i += 1
#     if i >=100:
#         print("100 osiągnięte")
#         break
#
#
# lista = [4, 5, 6]
# lista += [1, 2, 3]
# lista.append(4)
# lista.pop()
# print(lista)

# lista_silnia = []
# n = 20
# i = 1
# silnia = 1
#
# while i <= n:
#     silnia *= i
#     i += 1
#     lista_silnia.append(silnia)
#
# print(lista_silnia)

# fib = [0, 1]
# n = 20
# i = 1
#
# while i <= 20:
#     fib.append(fib[-1]+fib[-2])
#     i += 1
#
# print(fib)

# lista = []
# i = 0
# while i < 100:
#     i += 1
#     lista.append(i)
#
# print(lista)
# print(len(lista))

# lista = [1, 2, 3, 4, 5, 4, 4, 4, 4]
#
# lista.remove(4)
# del lista[3]
# print(lista)
#
# while 4 in lista:
#     lista.remove(4)
#
# print(lista)

# n = 100
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbizz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("bizz")
#     else:
#         print(i)

def powitaj(imie, nazwisko):
    print(f"Hello {imie} {nazwisko}")

powitaj("Krzysztof", "Nowak")
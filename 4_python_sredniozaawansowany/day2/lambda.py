# Zadanie
# Przy pomocy funkcji reduce znajdź w liście element największy.

from functools import reduce
items = [13, 5, 6, 2, 8]
# print(reduce((lambda x, y: x if x > y else y), items))

# Zadanie
# Napisz funkcję, która jako argument przyjmuje listę, a zwraca listę
# sześcianów elementów listy wejściowej. Trzema sposobami.


def power3(items):
    new_list = []
    for x in items:
        new_list.append(x ** 3)
    return new_list
# print(power3(items))
# print(list(map((lambda x: x ** 3), items)))
# print([x ** 3 for x in items])


# Zadanie
# Napisz funkcję, która zwraca listę wszystkich niepodzielnych przez 3 liczb
# z zakresu [1, 100]. Trzema sposobami.

list100 = range(1, 100)

def not_divisive_by3(list100):
    newlist = []
    for x in list100:
        if x % 3 != 0:
            newlist.append(x)
    return newlist

# print(not_divisive_by3(list100))
# print(list(filter((lambda x: x % 3), list100)))
# print([x for x in list100 if x % 3])

# Zadanie
# Napisz funkcję, która przyjmuje dwa parametry: jednym jest lista, a drugim
# liczba całkowita z domyślną wartością równą 5. Powinna zwracać listę
# tych elementów, które nie przekroczyły wartości tego parametru. Trzema
# sposobami.

a = 5

def number_under(lst, a):
    new_list = []
    for x in lst:
        if x <= a:
            new_list.append(x)
    return new_list

# print(number_under(list100, a))
# print(list(filter(lambda x: x <= a, list100)))
# print([x for x in list100 if x <= a])

# Zadanie
# Napisz funkcję, która przyjmuje listę i zwraca ją w zmienionej formie: tam,
# gdzie liczba była parzysta teraz mamy napis „Parzysta”, a tam, gdzie
# nieparzysta – (niespodzianka) „Nieparzysta”. Trzema sposobami.

def odd_even(lst):
    new_list = []
    for x in lst:
        if x % 2:
            new_list.append('odd')
        else:
            new_list.append('even')
    return new_list

# print(odd_even(list100))
# print(list(map(lambda x: 'odd' if x % 2 else 'even', list100)))
# print(['odd' if x % 2 else 'even' for x in list100])

# Zadanie
# Napisz funkcję, która przyjmuje listę i zwraca sumę kwadratów parzystych
# elementów.

def sum_squere_even(lst):
    square = 0
    for x in lst:
        if x % 2 == 0:
            square += x ** 2
    return square

# print(sum_squere_even(list100))
# print(sum(list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, list100))))))
# print(sum([x ** 2 for x in list100 if x % 2 == 0]))

# Zadanie
# Stwórz listę z 10 losowymi wartościami z przedziału [-10; 10], a następnie
# posortuj ją rosnąco pod względem kwadratów elementów

from random import randint

lst = [randint(-10, 10) for x in range(10)]
# print(sorted(lst, key=lambda x: x ** 2))

# Zadanie 3
# Stwórz klasę Pies z atrybutami imię oraz wiek. Następnie stwórz listę, w
# której przechowasz kilka instancji tej klasy. Następnie, przy pomocy
# funkcji map przekształć listę tych instancji w listę ich ludzkich lat.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dogs = [Dog('Fluffy', 12), Dog('Knickers', 3), Dog('Lessie', 10)]
# print(list(map(lambda x: x.age * 7, dogs)))

# Zadanie 4
# Stwórz 3 różne funkcje, które przyjmują jako argument listę, a zwracają
# iloczyn wszystkich jej dodatnich elementów.
import math

lst_pos = [-4, 3, 4, -2, 10]

def multiply_positive(lst):
    multi = 1
    for x in lst:
        if x > 0:
            multi *= x
    return multi

# print(multiply_positive(lst_pos))
# print(reduce(lambda x, y: x * y, list(filter(lambda x: x > 0, lst_pos))))
# print(math.prod([x for x in lst_pos if x > 0]))

# Zadanie 5
# Stwórz funkcję, która przyjmuje listę napisów i zwraca ją w postaci
# posortowanej, od najkrótszego do najdłuższego

list_word = ['one', 'two','three', 'four', 'five', 'six', 'eleven']
print(sorted(list_word, key=lambda x: len(x)))
print(sorted(list_word, key=len))
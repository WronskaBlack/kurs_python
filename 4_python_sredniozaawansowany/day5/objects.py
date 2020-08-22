from abc import ABC, abstractmethod
from math import pi

class Person:
    def __init__(self, name, surname, height, weight):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight
    def bmi(self):
        BMI = self.weight / self.height ** 2
        if BMI < 18.5:
            return "Underweight"
        elif BMI < 25:
           return "Normal (healthy weight)"
        elif BMI < 30:
            return "Overweight"
        else:
            return "Obese"
    def __str__(self):
        return f"{self.name} {self.surname} is {self.height}m tall and weights {self.height}kg"

mike = Person('Mike', 'Kowalski', 90, 1.8)
eve = Person('Eve', 'Johnson', 65, 1.65)
# print(eve)
# print(eve.bmi())

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    def __str__(self):
        return f"Osoba ma na imię {self.imie} i ma {self.wiek} lat"

class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        Osoba.__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin
    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin

class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        Osoba.__init__(self, imie, wiek)
        self.stypendium = stypendium
    def pokaz_finanse(self):
        return self.stypendium
    @classmethod
    def stworz_z_stringa(cls, napis):
        imie, wiek, stypendium = napis.split()
        wiek, stypendium = int(wiek), float(stypendium)
        return cls(imie, wiek, stypendium)
    @staticmethod
    def czy_imie_poprawne(imie):
        if imie[0].isupper() and len(imie) > 2:
            return True
        return False

class PracujacyStudent(Pracownik, Student):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)
    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin + self.stypendium

# jack = Pracownik('Jack', 40, 15, 10)
# print(jack)
# mark = Student('Mark', 23, 100)
# print(mark)
# print(mark.pokaz_finanse())
# print(jack.pokaz_finanse())
# rose = PracujacyStudent('Rose', 25, 10, 50, 300)
# print(rose)
# print(rose.pokaz_finanse())
# stud = Student.stworz_z_stringa("Maciej 21 500")
# print(stud)
# print(Student.czy_imie_poprawne('ala'))

class Figura(ABC):
    @abstractmethod
    def obwod(self):
        pass
    @abstractmethod
    def pole(self):
        pass

class Prosotkat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2 * (self.a + self.b)
    def pole(self):
        return self.a * self.b
    def __str__(self):
        return f"{self.a} {self.b}"
    def __repr__(self):
        return f"{self.a} {self.b}"

class Kolo(Figura):
    def __init__(self, r):
        self.r = r
    def obwod(self):
        return 2 * pi * self.r
    def pole(self):
        return pi * self.r ** 2

class Kwadrat(Prosotkat):
    def __init__(self, a):
        super().__init__(a, a)

prostokat = Prosotkat(3, 5)
kolo = Kolo(4)
kwadrat = Kwadrat(6)
# print(prostokat.obwod())
# print(kolo.obwod())
# print(kwadrat.pole())
# print(kwadrat.obwod())

# from copy import deepcopy
#
# p1 = Prosotkat(3, 4)
# lst = [1, p1, 3]
# lst2 = lst
# shallow_copy_lst = list(lst)
# deep_copy_lst = deepcopy(lst)
# print(lst)
# print(lst2)
# print(shallow_copy_lst)
# print(deep_copy_lst)
# lst[1].a = 5
# lst[0] = 2
# print()
# print(lst)
# print(lst2)
# print(shallow_copy_lst)
# print(deep_copy_lst)

import timeit
code = """
def func():
    return [sqrt(x) for x in range(100)]
"""
setup = "from math import sqrt"
# print(timeit.timeit(stmt=code, setup=setup))

import threading

def iterate_print(obj):
    for item in obj:
        print(item)


# t1 = threading.Thread(target=iterate_print, args=(range(5),))
# t2 = threading.Thread(target=iterate_print, args=("Pyhton",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# print("koniec")

# import requests
#
# def crawl(url, dest):
#     try:
#         result = requests.get(url).text
#         with open(dest, 'a') as f:
#             f.write(result)
#     except requests.exceptions.RequestException:
#         print('Error')
#
# def wo_threading_func(urls):
#     for url in urls:
#         crawl(url, "without_threads.txt")
#
# def with_threading_func(urls):
#     threads = []
#     for url in urls:
#         th = threading.Thread(target=crawl, args=(url, "with_thread.txt"))
#         th.start()
#         threads.append(th)
#     for th in threads:
#         th.join()
#
# if __name__ == "__main__":
#     setup = """
# from __main__ import wo_threading_func, with_threading_func
# urls = [
# 'https://jsonplaceholder.typicode.com/coments/1'
# 'https://jsonplaceholder.typicode.com/coments/2'
# 'https://jsonplaceholder.typicode.com/coments/3'
# ]
#     """
#     wo_threading = "wo_threading_func(urls)"
#     with_threading = "with_threading_func(urls)"
#
#     print("bez wątkiów: ", timeit.timeit(stmt=wo_threading, setup=setup, number=10))
#     print("z wątkiów: ", timeit.timeit(stmt=with_threading, setup=setup, number=10))


def count(from_, to_):
    while from_ > to_:
        from_ -= 1

def wo_threading_func():
    count(400000, 0)

def with_threading_func():
    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading = "with_threading_func()"

    setup = "from __main__ import wo_threading, with_threading"
    print("bez watlow :", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
    print("bez watlow :", timeit.timeit(stmt=with_threading, setup=setup, number=100))
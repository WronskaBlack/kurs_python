# from random import randint
#
# for i in range(10):
#     a = randint(0, 10)
#     b = randint(0, 2)
#     try:
#         wynik = a / b
#     except ZeroDivisionError:
#         wynik = 0
#     print(i, a, b, wynik)

def funkcja(lista):
    ind = 0
    while ind < len(lista):
        try:
            print(10 / lista[ind])
        except ZeroDivisionError:
            break
        ind += 1
    print(f'indeks: {ind}')


def funkcja2(lista):
    ind = 0
    while ind < len(lista):
        try:
            print(10 / lista[ind])
        except ZeroDivisionError:
            break
        finally:
            ind += 1
    print(f'indeks: {ind}')


# funkcja([2, 3, 5, 0, 4])
# funkcja2([2, 3, 5, 0, 4])
def birth_year():
    year = int(input('Podaj rok: '))
    return year < 2002

# try:
#     print(birth_year())
# except ValueError:
#     'niepoprawna data'



# months = {'january': 31, 'febuary': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'septeber': 30, 'october': 31, 'november': 30, 'december': 31}
# month_in = input('Month: ')
# try:
#     print(months[month_in])
# except KeyError:
#     print('Uncorrect month')


# Zadanie
# Napisz program, który wypisze na ekran zawartość pliku, którego nazwę
# podaje użytkownik.
# try:
#     f = open('file.txt', 'r')
#     print(f.readline())
# except FileNotFoundError:
#     print('File not found')

# Zadanie
# Napisz program, który zwróci wartość bezwzględną liczby pobranej od
# użytkownika. Program powinien pytać o tę liczbę tak długo, aż nie
# zostanie ona poprawnie podana.
# while True:
#     try:
#         number = int(input('Number: '))
#         break
#     except ValueError:
#         print('Enter a number!')
# print(abs(number))


# Zadanie
# Napisz program, który obliczy pole trójkąta na podstawie podanych przez
# użytkownika długości podstawy oraz wysokości, pod warunkiem, że obie
# te liczby są dodatnie.

# h = int(input('Enter height: '))
# b = int(input('Enter base: '))
# if h < 0 or b < 0:
#     raise ValueError("base and height can't be negative")
# print(h * b * 1/2)

# Zadanie
# Zmodyfikuj poprzednie zadanie, tworząc swój własny wyjątek.
# class NegativeNumber(Exception):
#     def __init__(self):
#         message = "base and height can't be negative"
#         super().__init__(message)
# h = int(input('Enter height: '))
# b = int(input('Enter base: '))
# if h < 0 or b < 0:
#     raise NegativeNumber
# print(h * b * 1/2)

# Zadanie
# Stwórz program, który pobiera od użytkownika liczbę z zakresu od 1 do
# 100 i losuje drugą, z zakresu od -5 do 5, a następnie dzieli pierwszą przez
# drugą. Pamiętaj o odpowiedniej obsłudze niepożądanych działań.
# from random import randint
# class NumberOutOfRange(Exception):
#     def __init__(self):
#         message = 'Number not in range 1-100'
#         super().__init__(message)
# number = int(input('Enter number between 1 and 100: '))
# if not(1 <= number <= 100):
#     raise NumberOutOfRange
# number2 = randint(-5, 5)
# try:
#     print(number / number2)
# except ZeroDivisionError:
#     print('Division by zero')


# Zadanie
# Stwórz program, który będzie pobierał od użytkownika liczby całkowite tak
# długo, aż ten nie wciśnie control+D – wówczas ma się pojawić informacja
# o tym, ile liczb całkowitych użytkownik podał, jaka jest ich suma oraz
# średnia.
numbers = []
while True:
    number = input('Enter number: ')
    if number == 'e':
        break
    numbers.append(int(number))
print(sum(numbers), sum(numbers)/len(numbers))

# Stwórz kalkulator BMI, a następnie wczuj się w złośliwego testera i
# zabezpiecz przed wszelkimi błędami, które użytkownik może celowo
# wprowadzić
# try:
#     weight = int(input('Enter weight: '))
#     height = int(input('Enter height: '))
#     print(weight / height ** 2)
# except ValueError:
#     print('Enter numbers')
# except ZeroDivisionError:
#     print("Height can't be zero")





# Zadanie 1.
# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
# na formę tekstową, np.:
# 112 - > „jeden jeden dwa”

def number2string(number):
    number_dict = {'0': 'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć', '6': 'sześć',
                   '7': 'siedem', '8': 'osiem', '9': 'dziewięć'}
    str_number = str(number)
    str_list = ''
    for i in str_number:
        str_list += number_dict[i] + ' '
    return str_list

# print(number2string(112))
# print(number2string(1234567890))
# print(number2string(5555))
# print(number2string(0))

# Zadanie 2.
# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program,
# który wskaże indeks najmniejszego z nich, iterując po nich.

def min_number(number_list):
    min_value = number_list[0]
    min_index = 0
    for i, num in enumerate(number_list):
        if num < min_value:
            min_value = num
            min_index = i
    return min_index

# print(min_number([-12, 0, 43]))
# print(min_number([12, 0, -43, 13, -23]))
# print(min_number([12, 0, 23, 13, -55]))

# Zadanie 3.
# Napisz program, który pobierze 5 słów od użytkownika, a następnie
# wypisze najdłuższe z nich.

# max_len = 0
# max_word = ''
# for i in range(5):
#     word = input('Podaj słowo: ')
#     if len(word) > max_len:
#         max_len = len(word)
#         max_word = word
# print(max_word)


# Zadanie 4.
# Napisz program, który obliczy liczbę małych i wielkich liter w ciągu.
# np : 'The quick Brown Fox'
# oczekiwany wynik :
# No. of Upper case characters : 3
# No. of Lower case Characters : 13


def lower_upper(string):
    lower, upper = 0, 0
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return f'No. of Upper case characters : {upper}\nNo. of Lower case Characters : {lower}'

# print(lower_upper('The quick Brown Fox'))


# Zadanie 5.
# Napisz program, który poprosi użytkownika o podanie słowa i napisze,
# czy jest ono izogramem (słowo, w którym żadna litera się nie powtórzyła,
# np. „skrzynia”)

def isizogram_count(word):
    for i in set(word):
        if word.count(i) > 1:
            return False
    return True

def isizogram_set(word):
    return len(word) == len(set(word))

# word = input('Podaj słowo: ')
# print(isizogram_count(word))
# print(isizogram_set(word))

# Zadanie 6.
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# palindromem (tj. czytany od przodu i wspak jest dokładnie taki sam, np.
# „kajak”, „Madam”, „nurses run”).

def is_palindrom(word):
    word_r = word.replace(' ','')
    word_l = word_r.lower()
    return word_l == word_l[::-1]

#print(is_palindrom('Nurses run'))


# Zadanie 7.
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# pangramem (tj. zawiera każdą literę alfabetu co najmniej raz, np. „The
# quick brown fox jumps over the lazy dog”).

def is_pangram(words):
    n_words = words.lower()
    return len(set(n_words)) >= 26

# print(is_pangram('The quick brown fox jumps over the lazy dog'))


# Zadanie 8.
# Napisz funkcję, która sprawdzi, czy podana liczba jest doskonała (tj. jest
# sumą swoich dzielników właściwych, np. 6 = 1 + 2 + 3).

def is_perfect(number):
    divisors = 0
    for i in range(1, number):
        if number % i == 0:
            divisors += i
    return divisors == number

# print(is_perfect(28))

# Zadanie 9.
# Napisz funkcję, która obliczy wartość zadanego elementu ciągu
# Fibonacciego rekurencyjnie i iteracyjnie.

def fib_iter(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]

def fib_rek(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib_rek(n-1) + fib_rek(n-2)

# print(fib_iter(8))
# print(fib_rek(8))

# Zadanie 10.
# Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza
# https://pastebin.com/raw/aAHeW5Pt

mickiewicz = """Bez serc bez ducha to szkieletów ludy
Młodości dodaj mi skrzydła
Niech nad martwym wzlecę światem
W rajską dziedzinę ułudy
Kędy zapał tworzy cudy
Nowości potrząsa kwiatem
I obleka w nadziei złote malowidła

Niechaj kogo wiek zamroczy
Chyląc ku ziemi poradlone czoło
Takie widzi świata koło
Jakie tępymi zakreśla oczy

Młodości ty nad poziomy
Wylatuj a okiem słońca
Ludzkości całe ogromy
Przeniknij z końca do końca

Patrz na dół  kędy wieczna mgła zaciemia
Obszar gnuśności zalany odmętem
To ziemia
Patrz jak nad jej wody trupie
Wzbił się jakiś płaz w skorupie
Sam sobie sterem żeglarzem okrętem
Goniąc za żywiołkami drobniejszego płazu
To się wzbija to w głąb wali
Nie lgnie do niego fala ani on do fali
A wtem jak bańka prysnął o szmat głazu
Nikt nie znał jego życia nie zna jego zguby
To samoluby

Młodości tobie nektar żywota
Natenczas słodki gdy z innymi dzielę
Serca niebieskie poi wesele
Kiedy je razem nić powiąże złota

Razem młodzi przyjaciele
W szczęściu wszystkiego są wszystkich cele
Jednością silni rozumni szałem
Razem młodzi przyjaciele
I ten szczęśliwy kto padł wśród zawodu
Jeżeli poległym ciałem
Dał innym szczebel do sławy grodu
Razem młodzi przyjaciele
Choć droga stroma i śliska
Gwałt i słabość bronią wchodu
Gwałt niech się gwałtem odciska
A ze słabością łamać uczmy się za młodu

Dzieckiem w kolebce kto łeb urwał Hydrze
Ten młody zdusi Centaury
Piekłu ofiarę wydrze
Do nieba pójdzie po laury
Tam sięgaj gdzie wzrok nie sięga
Łam czego rozum nie złamie
Młodości orla twych lotów potęga
Jako piorun twoje ramię

Hej ramię do ramienia spólnymi łańcuchy
Opaszmy ziemskie kolisko
Zestrzelmy myśli w jedno ognisko
I w jedno ognisko duchy
Dalej bryło z posad świata
Nowymi cię pchniemy tory
Aż opleśniałej zbywszy się kory
Zielone przypomnisz lata

A jako w krajach zamętu i nocy
Skłóconych żywiołów waśnią
Jednym stań się z bożej mocy
Świat rzeczy stanął na zrębie
Szumią wichry cieką głębie
A gwiazdy błękit rozjaśnią 

W krajach ludzkości jeszcze noc głucha
Żywioły chęci jeszcze są w wojnie
Oto miłość ogniem zionie
Wyjdzie z zamętu świat ducha
Młodość go pocznie na swoim łonie
A przyjaźń w wieczne skojarzy spojnie

Pryskają nieczułe lody
I przesądy światło ćmiące
Witaj jutrzenko swobody
Zbawienia za tobą słońce"""

mck_lst = mickiewicz.lower().split()
count = []
for word in set(mck_lst):
    count.append([word, mck_lst.count(word)])
count.sort(key=lambda x: x[1], reverse=True)
# for i in range(5):
#     print(count[i][0])

# Zadanie 11.
# Stwórz klasę reprezentującą koło o danym promieniu z metodami do obliczania jego pola
# powierzchni i obwodu. Odpowiednią stałą zaimportuj z zewnętrznego modułu.
from math import pi

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * self.r ** 2
    def perimeter(self):
        return 2 * pi * self.r

new_circle = Circle(5)

# print(new_circle.area(), new_circle.perimeter())

# Zadanie 12.
# Napisz funkcję która policzy sumę cyfr liczby, nie zamieniając jej na
# stringa, ani listę. Rekurencyjnie oraz iteracyjnie.
# np. 123 → 1+2+3 = 6

def sum_rec(number):
    if number // 10 == 0:
        return number % 10
    return sum_rec(number // 10) + number % 10

def sum_iter(number):
    s = 0
    while True:
        if number // 10 != 0:
            s += number % 10
            number = number // 10
        else:
            s += number % 10
            break
    return s

# print(sum_rec(123))
# print(sum_iter(123))

# Zadanie 13.
# Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi
# anagramami.

def anagram(str1, str2):
    word1 = str1.lower().replace(' ', '')
    word2 = str2.lower().replace(' ', '')
    return sorted(word1) == sorted(word2)

# print(anagram('Tom Marvolo Riddle', 'I am Lord Voldemort'))

# Zadanie 14.
# Stwórz klasę Punkt, która będzie reprezentować punkt w układzie
# współrzędnych. Chcemy móc wyświetlić jego reprezentację na ekranie,
# przesunąć o dany wektor oraz obliczyć odległość od innego punktu.
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        plt.plot(self.x, self.y, 'or')
        plt.show()
    def move(self, x, y):
        self.x += x
        self.y += y
    def distance(self, p):
        return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** (1/2)

# p1 = Point(1, 2)
# p1.show()
# p1.move(2, 3)
# p1.show()
# p2 = Point(5, 5)
# p2.show()
# print(p1.distance(p2))

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

print(fib_iter(8))
print(fib_rek(8))
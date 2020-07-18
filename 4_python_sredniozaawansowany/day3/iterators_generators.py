from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

class PrimeIter:
    def __init__(self, n):
        self.n = n
        self.generated_number = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_number == self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_number += 1
            return self.number
        return self.__next__()



# for i in PrimeIter(10):
#     print(i)

def prime_generator(n):
    number = 2
    generated_number = 0
    while generated_number != n:
        if is_prime(number):
            yield number
            generated_number += 1
        number += 1

# for i in PrimeIter(10):
#     print(i)

class SumIterator:
    def __init__(self, n):
        self.n = n
        self.number = 0
        self.generated_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_number == self.n:
            raise StopIteration
        self.generated_number += 1
        self.number += self.generated_number
        return self.number

def sum_generator(n):
    number = 0
    generated_number = 0
    while generated_number != n:
        generated_number += 1
        number += generated_number
        yield number

# for i in sum_generator(10):
#     print(i)
# print()
# for i in SumIterator(10):
#     print(i)

class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.n:
            raise StopIteration
        self.number += 1
        return self.number ** 2

def square_generator(n):
    number = 0
    while number != n:
        number += 1
        yield number ** 2

# for i in SquareIterator(10):
#     print(i)
# print()
# for i in square_generator(10):
#     print(i)

class FibbIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number2 = 0
        self.number1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers == self.n:
            raise StopIteration
        self.generated_numbers += 1
        self.number2, self.number1 = self.number1, self.number2 + self.number1
        return self.number2

def fibb_generator(n):
    number2 = 0
    number1 = 1
    generated_numbers = 0
    while generated_numbers != n:
        generated_numbers += 1
        number2, number1 = number1, number2 + number1
        yield number2


# for i in fibb_generator(10):
#     print(i)
# print()
# for i in FibbIterator(10):
#     print(i)

class NotDividedIterator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.number = 0
        self.numbers_generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.numbers_generated == self.n:
            raise StopIteration
        elif self.number % self.m != 0:
            self.numbers_generated += 1
            return self.number
        return self.__next__()

def not_divided_generator(n, m):
    number = 0
    numbers_generated = 0
    while numbers_generated != n:
        number += 1
        if number % m != 0:
            numbers_generated += 1
            yield number

for i in not_divided_generator(10, 3):
    print(i)
print()
for i in not_divided_generator(10, 3):
    print(i)




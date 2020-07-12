def is_palindrom(value):
    # delete special chars and lower cases
    text = ''.join(filter(str.isalnum, value)).lower()
    return text == text[::-1]


def count_even_odd(numbers):
    even = 0
    odd = 0
    for n in numbers:
        try:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
        except ZeroDivisionError:
            pass
    return {'count_even': even, 'count_odd': odd}


def find_max3(numbers):
    numbers.sort(reverse=True)
    max_positive = numbers[0] * numbers[1] * numbers[2]
    max_negative = numbers[0] * numbers[-1] * numbers[-2]
    return max(max_positive, max_negative)


class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def add_cash(self, cash):
        self.balance += cash

    def spend_cash(self, cash):
        if self.balance - cash < 0:
            raise Exception
        self.balance -= cash

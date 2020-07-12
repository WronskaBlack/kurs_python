import os
import requests


def is_even(number):
    return number % 2 == 0


class Account:
    def __init__(self, name, surname, number, balance=0):
        self.name = name
        self.surname = surname
        self.ac_number = number
        self.ac_balance = balance

    def owner(self):
        return f'{self.name} {self.surname}'

    def number(self):
        return self.ac_number

    def balance(self):
        return self.ac_balance

    def transfer(self, value):
        if self.ac_balance + value < 0:
            raise Exception
        self.ac_balance += value


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_name_with_title(self, title):
        return f'{title} {self.name} {self.surname}'


def remove_file(file_name):
    os.remove(file_name)


def is_correct_website(web):
    result = requests.get(web)
    if 200 <= result.status_code < 400:
        return True
    return False

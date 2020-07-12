"""
Napisz funkcję która doda klucz i wartość do słownika
"""
slownik = {}


def add_key_value(key, value):
    slownik[key] = value
    pass


add_key_value('cat', 'kot')
add_key_value('dog', 'pies')
print(slownik)

"""
slownik = {
  'cat': 'kot',
  'dog': 'pies'
}
"""
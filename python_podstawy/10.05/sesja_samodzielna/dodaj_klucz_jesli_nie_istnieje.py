"""
Napisz funkcję która doda klucz i wartość do słownika
tylko jeśli takiego klucza wcześniej w nim nie było

Wykorzystaj 'klucz' in slownik do sprawdzenia czy klucz w słowniku już jest
True jeśli już taki klucz istnieje
False jeśli klucza jeszcze nie ma
"""
slownik = {}


def add_unique_key_value(key, value):
    if key not in slownik:
        slownik[key] = value
    pass


add_unique_key_value('cat', 'kot')
add_unique_key_value('cat', 'pies')
print(slownik)
# powinien być tylko {'cat': 'kot'}

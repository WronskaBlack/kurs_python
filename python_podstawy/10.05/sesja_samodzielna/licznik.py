"""
Policz ilośc wystąpień znaków w stringu.
'aaab' => {'a':3,'b':1'}

Mozna użyc sprawdzenia czy coś znajduje się w słowniku poprzez
'klucz' in slownik
zwróci True jeśli jest, False jeśli nie jest
"""
def licznik(ciag_znakow):
    slownik = {}
    for i in set(ciag_znakow):
        slownik[i] = ciag_znakow.count(i)
    return slownik


print(licznik('aaab'))
assert licznik('aaab') == {'a': 3, 'b': 1}



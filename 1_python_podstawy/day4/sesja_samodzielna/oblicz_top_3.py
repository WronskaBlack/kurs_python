"""
Zwróc listę top 3 wyrazów w tekście
tekst = "kot kot kot kot pies pies pies zółw zółw małpa"
['kot', 'pies', 'zółw']
Kolejność ich występowania nie ma znaczenia
słowa oddzielone są zawsze spacją
"""


def top_3(tekst):
    lista = tekst.split()
    zliczanie = []
    for i in set(lista):
        print(i)
        zliczanie.append([i, lista.count(i)])
    print(zliczanie)
    zliczanie = sorted(zliczanie, key=lambda x: x[1], reverse=True)
    wyniki = [zliczanie[0][0], zliczanie[1][0], zliczanie[2][0]]

    return wyniki


top_3_wynik = top_3("kot kot kot kot pies pies pies zółw zółw małpa")
print(top_3_wynik)

assert 'kot' in top_3_wynik
assert 'pies' in top_3_wynik
assert 'zółw' in top_3_wynik
assert 'małpa' not in top_3_wynik

"""
Oblicz średnią ocen wszystkich uczniów w klasie
Oblicz srednia dla kazdego
a zsumuj i na koniec podziel przez ilosc uczniow
"""
oceny = {
    'Krzysztof': [1, 2, 3, 4, 1, 1, 1, 2],
    'Andrzej': [2, 3, 2, 1, 5, 6, 6, 3],
    'Dominik': [4, 5, 3, 2, 1, 2, 3, 4]
}


srednia = []

for imie, lista in oceny.items():
   srednia.append(sum(lista)/len(lista))

srednia_calej_klasy = sum(srednia)/len(srednia)
print(srednia)
print(srednia_calej_klasy)

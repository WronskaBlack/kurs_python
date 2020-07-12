"""
Zamien oceny na słownik
{
   "imie": [<lista ocen>]
}
"""
oceny = [
    ['Krzysztof', 1, 2, 1, 2, 1],
    ['Andrzej', 2,1,2,4,5,3,2,1],
    ['Dominika', 6,5,4,5,6,5,4]
]
slownik = {}

for lista in oceny:
    slownik[lista[0]] = lista[1:]


print(slownik)
print(slownik['Krzysztof'])
print(slownik['Andrzej'])
print(slownik['Dominika'])

"""
Nowy słownik srednie, zawiera imie oraz średnią ocen każdego ucznia
srednie = {
   'Krzysztof': 1.1,
   ...
    'Dominika': 5.5
}
suma ocen/ilosc ocen
"""
srednie = {}
for imie, oceny in slownik.items():
    srednie[imie] = sum(oceny) / len(oceny)

print(srednie)
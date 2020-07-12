"""
Zwróć listę 3 największych przedmiotów ze słownika
{
    'chleb': 1000,
    'bułka': 0,
    'samochód': 100000992,
    'dom': 9999999999
}

zwróć, kolejność nie ma znaczenia
['chleb', 'samochod', 'dom']
"""
import operator
top_3 = []
items = {
    'chleb': 1000,
    'bułka': 1,
    'samochód': 100000992,
    'dom': 999999999999999
}
for i in range(3):
    maxi = max(items.items(), key=operator.itemgetter(1))[0]
    top_3.append(maxi)
    del items[maxi]


print(top_3)
# powinno wyświetlić ['chleb', 'samochod', 'dom']
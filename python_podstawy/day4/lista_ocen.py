lita_ocen = [2, 3, 2]
lista_przedmiotow = ["matematyka", "fizyka", "muzyka"]
oceny_krzysztofa = {}

assert len(lita_ocen) == len(lista_przedmiotow)

for i in range(len(lita_ocen)):
    oceny_krzysztofa[lista_przedmiotow[i]] = lita_ocen[i]

print(oceny_krzysztofa["matematyka"])
print(oceny_krzysztofa["fizyka"])
print(oceny_krzysztofa["muzyka"])
import json
lista_uczniow = ["Krzysztof", "Andrzej"]
obecnosci = {}
dodaj_nowe = "y"
while dodaj_nowe == "y":
    data = input("Podaj datę zajęć: ")
    obecni_tego_dnia = []
    for uczen in lista_uczniow:
        czy_obecny = input(f"Czy był obecny {uczen}? ")
        if czy_obecny == "y":
            obecni_tego_dnia.append(uczen)
    obecnosci[data] = obecni_tego_dnia
    dodaj_nowe = input("Czy kontynuować? ")

print(obecnosci)

with open("lista_obecnosci.txt", "w") as file:
    file.write(str(obecnosci))

with open("lista_obecnosci.json", "w") as file:
    file.write(json.dumps(obecnosci))

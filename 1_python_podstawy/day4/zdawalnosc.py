szkola = {
    "krzysztof": {"obecnosci": ["20.04"], "oceny": [4, 5]},
    "andrzej": {"obecnosci": ["20.04","21.04","23.04"], "oceny": [1, 2, 4, 1, 6]}
}
zdawalnośc = 2
ilosc_zajec = 3

for imie, slownik in szkola.items():
    obecnosci = len(slownik["obecnosci"])
    oceny = slownik["oceny"]
    srednia = sum(oceny)/len(oceny)
    if srednia > zdawalnośc and obecnosci > ilosc_zajec/2:
        print(imie, "zdaje")
    else:
        print(imie, "nie zdaje")
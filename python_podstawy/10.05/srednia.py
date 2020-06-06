oceny_z_fizyki = {
    "Krzysztof": [2, 2, 1, 2, 1, 1, 1, 2, 4, 1, 1, 3],
    "Andrzej": [5, 3, 4, 3, 2, 3]
}
zdawalnosc = 2
for imie, oceny in oceny_z_fizyki.items():
    srednia = sum(oceny)/len(oceny)
    print(f"{imie} ma średnią {srednia:.2f}")
    if srednia > zdawalnosc:
        print("zdaje")
    else:
        print("nie zdaje")

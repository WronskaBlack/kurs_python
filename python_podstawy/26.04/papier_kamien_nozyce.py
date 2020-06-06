import random
gramy = True
mozliwosc = ["p", "k", "n"]

while gramy:
    komp = random.choice(mozliwosc)
    gracz = input("Podaj k/p/n: ").lower()
    if  gracz not in mozliwosc:
        print("Zła wartość.")
        continue
    print(komp)
    if gracz == komp:
        print("remis")
    elif gracz == "k":
        if komp == "n":
            print("wygrałeś")
        else:
            print("przegrałeś")
    elif gracz == "n":
        if komp == "k":
            print("przegrałeś")
        else:
            print("wygrałeś")
    else:
        if komp == "k":
            print("wygrałeś")
        else:
            print("przegrałeś")



    gramy_dalej = input("czy chcesz grać dalej t/n: ").lower()
    if gramy_dalej == "t":
        continue
    else:
        break
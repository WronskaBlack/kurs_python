def nawiasy(nawias):
    otwarte = 0
    for i in nawias:
        if i == "[":
            otwarte += 1
        elif i == "]":
            otwarte -= 1
            if otwarte < 0:
                return False
    if otwarte == 0:
        return True
    else:
        return False



nawias = input("Podaj ciąg nawiasów: ")

print(nawiasy(nawias))

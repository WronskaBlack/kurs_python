L = [["Chemia", 1], ["Fizyka", 2], ["Matematyka", 4]]
oceny = {}
for para in L:
    oceny[para[0]] = para[1]
print(oceny)

oceny_2 = {}

for key, value in L:
    oceny_2[key] = value

print(oceny_2)
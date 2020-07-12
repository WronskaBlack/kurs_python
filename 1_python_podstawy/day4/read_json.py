import json

with open("lista_obecnosci.json") as file:
    lista_obecnosc = json.load(file)

print(lista_obecnosc)
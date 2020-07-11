"""
Napisz funkcję, która usunie z listy podanej jako argument
wszystkie wyrazy zawierające podaną frazę.

można użyć 'cos' in cos_innego
"""
def del_word(li, word):
    li2 = []
    for i in li:
        print(i)
        if word.lower() not in i.lower():
           li2.append(i)
    return li2

L = [
    'krowa',
    'pies',
    'kot',
    'zółw jest wolny',
    'kot zdradziecki',
    'KOT'
]
print(L)
print(del_word(L, "kot"))


"""
np. tak
def usuwanie(lista, fraza)
"""




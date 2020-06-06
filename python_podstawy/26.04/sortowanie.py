lista = [5, 4, 36, 446353, 2937, -222, 32723, 32, 435, -352, 31, 5757, 5, 65, 7, -34, 54]
bubble = list(lista)
select = list(lista)
s_insert = list(lista)
print(lista)

# sortowanie bąbelkowe / bubble sort
zmiana = True
while zmiana:
    zmiana = False
    for i in range(1, len(bubble)):
        if bubble[i - 1] > bubble[i]:
            temp = bubble[i - 1]
            bubble[i - 1] = bubble[i]
            bubble[i] = temp
            zmiana = True
print(bubble)

# sortowanie przez wybór / selection sort
for j in range(0, len(select)):
    mini = j
    for i in range(j, len(select)):
        if select[i] < select[mini]:
            mini = i
    temp = select[j]
    select[j] = select[mini]
    select[mini] = temp
print(select)

#sortowanie przez wstawianie / insertion sort
for i, el in enumerate(s_insert[1:], 1):
    for j, jel in enumerate(s_insert[:i + 1]):
        if el < jel:
            s_insert.pop(i)
            s_insert.insert(j, el)
            break
print(s_insert)


# sortowanie w pythonie
lista.sort()
print(lista)
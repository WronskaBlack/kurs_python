a = 0
b = 1
print(a)
print(b)

i = 0
while i < 20:
    i += 1
    c = a + b
    print(c)
    a = b
    b = c

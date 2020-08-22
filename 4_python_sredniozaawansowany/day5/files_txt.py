import os

# f = open('file.txt', 'a+')
# print(f.read())
# f.write('\nPython is cool')
# f.close()

# with open('in.txt', 'r') as f_in, open('out.txt', 'w') as f_out:
#     for line in f_in.readlines():
#         f_out.writelines(line.capitalize())

if os.path.isfile('pan_tadeusz.txt'):
    with open('pan_tadeusz.txt') as tadek:
        print(tadek.read())
else:
    with open('pan_tadeusz.txt', 'w') as tadek:
        tadek.write("""Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.""")
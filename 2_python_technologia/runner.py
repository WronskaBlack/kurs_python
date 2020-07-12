# import test_module    # imports module from the same directory
# test_module.print_my_name("Jagoda")
# test_module.print_my_name(test_module.print_my_name())


# import test_module as tm  # imports module with different prefix
# tm.print_my_name("Jagoda")
# tm.print_my_name(tm.my_new_name)


# from test_module import my_new_name # imports only my_new_name, no need for prefix
# my_new_name = "Jagoda"    # replacing var from module, be careful with names
# print(my_new_name)

# from test_module import *     # imports all from module DON'T DO THAT
# print_my_name(my_new_name)

# standard modules
import csv

# installed modules
# import django
# import pandas

# local modules
from app import print_functions     # imports module from subfolder, that's the way to go
from app import print_functions2

print_functions.print_numbers(5)
names = ["Asia", "Ola", "Tomek"]
print_functions.print_names(names)
print_functions2.print_names(names)

print(__name__)
print(print_functions.__name__)

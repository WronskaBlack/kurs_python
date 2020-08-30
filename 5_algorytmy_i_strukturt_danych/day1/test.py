# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def get(self):
#         pass
#
# class B(A):
#     def set(self):
#         return 'B'
#
# b = B()
# print(b.set())

# assert sum([1, 1, 1]) == 6, "Should be 6"

# print(sum([1, 1, 2]))

# from json import dumps
#
# print(type(dumps({'key': 'val'})))
#
# a=[1,2]
# b=[x**2 for x in a if x<2]
# print(b)

#
# from operator import add, sub
# d = {
#     'add': add,
#     'sub': sub
# }
# print(d.get('mul', add)(5,4))

# a = lambda x: lambda y: x+y
#
# print(a(3)(5))
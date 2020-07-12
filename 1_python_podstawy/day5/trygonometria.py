"""
Utwórz klasy które pomogą obliczyć pole i obwód dla
1. trójkąta
2. prostokąta
3. koła


Kiedy wywołamy print na obiekcie, pojawi sie opis jaka to figura
oraz jej pole i obwód.
t1 = Trojkat(2,3)
print(t1) #  => "Trójkąt, pole: 123, obwód: 12"
"""


class Triangle:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return self.a * self.h / 2

    def __str__(self):
        return f"Trójkąt o obwodzie {self.perimeter()} i polu {self.area()}."


class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2

    def __str__(self):
        return f"Kwadrat o obwodzie {self.perimeter()} i polu {self.area()}."


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Prostokąt o obwodzie {self.perimeter()} i polu {self.area()}."


tr = Triangle(2, 3, 4, 4)
sq = Square(3)
rec = Rectangle(3, 5)
print(tr)
print(sq)
print(rec)

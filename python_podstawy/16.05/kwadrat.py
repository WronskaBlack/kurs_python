class Square():
    def __init__(self, a):
        self.a = a
    def circumference(self):
        return 4*self.a
    def area(self):
        return self.a ** 2

sqr = Square(2)

print(sqr.circumference())
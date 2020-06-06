class Animal():
    age = 0
    def __init__(self, name):
        self.name = name

    def birthday(self):
        self.age += 1
    def __str__(self):
        return self.name
class Dogo(Animal):
    def hello(self):
        print(f"Cześć jestem {self.name}.")


dog1 = Dogo("Lessie")
print(dog1.name)
dog1.hello()
dog1.birthday()
print(dog1.age)

dog2 = Dogo("Burek")
print(dog1)

def dzielenie_input():
    try:
        return int(input())
    except:
        dzielenie_input()

dzielnik = dzielenie_input()
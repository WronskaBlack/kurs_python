english_to_polish = {"book": "książka", "cat": "kot", "car":"samochód"}

print(english_to_polish.keys())

def przetlumacz(angielskie):
    return english_to_polish[angielskie]

print(przetlumacz("book"))
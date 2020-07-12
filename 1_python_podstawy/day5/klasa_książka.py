class Book:
    amount = 100
    profit = 0
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
    def sell(self):
        if self.amount > 0:
            self.amount -= 1
            self.profit += self.price


potter = Book("Rowling", "Harry Potter", 45.99)
potter.amount = 50
potter.sell()
print(potter.profit, potter.amount)
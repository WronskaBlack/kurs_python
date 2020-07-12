class Band():
    def __init__(self, name):
        self.name = name
class Record():
    def __init__(self, band, title, price):
        self.band = band
        self.title = title
        self.price = price

metallica = Band("Metallica")
master = Record(metallica, "Master of Puppets", 39.99)
print(master.band.name)
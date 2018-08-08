class PriceRepository:
    def __init__(self):
        self.list = []

    def add(self, price):
        self.list.append(price)

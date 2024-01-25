class Item:
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def profit(self):
        return self.price - self.cost

    def applySale(self, percent):
        self.price = self.price * (1 - percent / 100)

    def __str__(self):
        return f"{self.name} (cost: ${self.cost}, price: ${self.price})"

class Clothing(Item):
    def __init__(self, name, cost, price, brand, size):
        super().__init__(name, cost, price)
        self.brand = brand
        self.size = size

    def get_brand(self): 
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def __str__(self):
        return f"{self.name} (brand: {self.brand}, size: {self.size}, cost: ${self.cost}, price: ${self.price})"

class Food(Item):
    def __init__(self, name, cost, price, shelfLife=7):
        super().__init__(name, cost, price)
        self.shelfLife = shelfLife

    def get_shelfLife(self):
        return self.shelfLife

    def set_shelfLife(self, shelfLife):
        self.shelfLife = shelfLife

    def __str__(self):
        return f"{self.name} (shelf life: {self.shelfLife} days, cost: ${self.cost}, price: ${self.price})"

class Shoe(Clothing):
    def __init__(self, cost, price, size):
        super().__init__("Crocs", cost, price, "Nike", size)

class Chips(Food):
    def __init__(self):
        super().__init__("Lays", 2, 3.50, 21)

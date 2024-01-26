#####################################################################
# author:   Satyendra Raj Singh    
# date:   01/24/2024      
# description: The above below defines several classes including Item, Clothing, Food, Shoe, and Chips, each with their own properties and methods.
#####################################################################

# An Item has a name, cost and price, all of which are passed in as
# arguments to its constructor. It has accessors and mutators that carry
# out range checking. It also has profit, applySale, and __str__
# functions that carry out the tasks as described in the assignment
# documentation.
class Item:
    def __init__(self,name,cost,price):
        self._name = name
        self._cost = cost
        self._price = price

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,names):
        self._name = names

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self,costs):
        if costs >= 0:
             self._cost=costs 
        else:
            self._cost = 0
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,prices):
        if prices(self,prices):
            self._price = prices
        else:
            self._price = 0
    
    def profit(self):
        return self._price-self._cost

    def applySale(self,DisPercent):
        if DisPercent > 0 :
            reduce = (DisPercent/100) * self._price
            self._price = reduce


    def __str__(self):
        return "{:<10} {:<10.2f} {:<10.2f}".format(self._name,self._cost, self._price)
        # return f"{self.name}\t {self.cost:.2f}\t{self.price:.2f}"



#####################################################################
# A Clothing is an Item. In addition to name, cost and price, it also
# has a brand, and size. It receives all 5 pieces of information as
# arguments to its constructor. It overloads the __str__ function and
# also has appropriate accessors and mutators.
class Clothing(Item):
    def __init__(self,name,cost,price,brand,size):
        super().__init__(name, cost, price)
        self._brand = brand
        self._size = size if size >= 0 else 0

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self,brand):
        self._brand = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size >= 0:
            self._size = size
        else:
            self._size = None
    
    def __str__(self):
        return "{}|{:<5}  size:{}".format(super().__str__(), self._brand, self._size)
        

#####################################################################
# A Food is an Item. In addition to name, cost and price, it also has a
# shelfLife. It only receives name, cost and price as arguments to its
# constructor. It sets all objects created to have a shelfLife of 7 by
# default. It also overloads the __str__ function.
class Food(Item):
    def __init__(self,name,cost,price,shelf_Life=7):
        super().__init__(name, cost, price)
        self.shelf_Life = shelf_Life

    @property
    def shelf_Life(self):
        return self._shelf_Life

    @shelf_Life.setter
    def shelf_Life(self,value):
        # self.shelfLife = shelfLife
        if value >= 0:
            self._shelf_Life = value
        else:
            self._shelf_Life = None

    def __str__(self):
            return "{}|expires in {} days".format(super().__str__(), self._shelf_Life)
            

#####################################################################
# A Shoe is a Clothing. It only receives cost, price and size as
# arguments to its constructor. It sets all Shoe objects to have a name
# of "Sneakers" and brand of "Nike" by default.
class Shoe(Clothing):
    def __init__(self, cost, price, size, brand="Nike"):
        super().__init__("Crocs",cost, price, brand, size)


#####################################################################
# A Chips is a Food. It does not receive any arguments for its
# constructor. It sets the name, cost, price and shelfLife to be "Lays",
# 2, 3.50 and 21 respectively.
class Chips(Food):
    def __init__(self):
        super().__init__("Lays", 2.00, 3.50, 21)


#####################################################################

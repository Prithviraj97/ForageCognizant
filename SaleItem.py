#####################################################################
# author:       
# date:         
# description: 
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
        return "{:<15} {:>15} {:>15}".format(self._name,self._cost, self._price)

    

        

    

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
    def brand(self,brands):
        self._brand = brands

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,sizes):
        if sizes >= 0:
            self._size = sizes
        else:
            sizes = 0
    
    def __str__(self):
        return "{} {} {}".format(super().__str__(), self._brand, self._size)
        





    

#####################################################################
# A Food is an Item. In addition to name, cost and price, it also has a
# shelfLife. It only receives name, cost and price as arguments to its
# constructor. It sets all objects created to have a shelfLife of 7 by
# default. It also overloads the __str__ function.
class Food(Item):
    def __init__(self,name,cost,price,shelfLife=7):
        super().__init__(name, cost, price)
        self._shelfLife = shelfLife

    @property
    def shelfLife(self):
        return self._shelfLife

    @shelfLife.setter
    def shelfLife(self,shelfLife):
        self._shelfLife = shelfLife
        # if value >= 0:
        #     self._shelfLife = value
        # else:
        #     self._shelfLife = 7

        def __str__(self):
            return "{:<15}Expires in {:>15} days".format(__str__(), self._shelfLife)
            


#####################################################################
# A Shoe is a Clothing. It only receives cost, price and size as
# arguments to its constructor. It sets all Shoe objects to have a name
# of "Sneakers" and brand of "Nike" by default.
class Shoe(Clothing):
    def __init__(self, cost, price, size):
        super().__init__("Crocs", "Nike", cost, price, size)

class Chips(Food):
    def __init__(self):
        super().__init__("Lays", 2, 3.50, 21)


#####################################################################
# A Chips is a Food. It does not receive any arguments for its
# constructor. It sets the name, cost, price and shelfLife to be "Lays",
# 2, 3.50 and 21 respectively.


#####################################################################

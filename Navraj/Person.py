#####################################################################
# author:      
# date:        
# description: 
#####################################################################

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person:


    def __init__(self, name="player 1", x=0, y=0, size=1.0):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self._name = value
        else:
            self._name = "player 1"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        elif value > MAX_X:
            self._x = MAX_X
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            self._y = 0
        elif value > MAX_Y:
            self._y = MAX_Y
        else:
            self._y = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value >= 1:
            self._size = value

    def goLeft(self, value=1):
        self.x -= value

    def goRight(self, value=1):
        self.x += value

    def goUp(self, value=1):
        self.y -= value

    def goDown(self, value=1):
        self.y += value

    def getDistance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        if 0 <= self.x <= MAX_X and 0 <= self.y <= MAX_Y:
            return f'p{self.name[-1]}:Person({self.name}): size = {self.size}, x = {self.x} y = {self.y}'
        else:
            return f'p{self.name[-1]}:Person({self.name}): size = {self.size}, x = {self.x} y = {self.y} '






    

        







    

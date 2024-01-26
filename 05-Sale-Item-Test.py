#####################################################################
# author:       anky
# date:         17th Jan, 2023.
# description:  A file to test out the Item class and its subclasses.
#####################################################################

# Import all the classes from the file named SaleItem.py
from SaleItem import * 

# Create 3 basic items and print them
i1 = Item("bananas", 2, 4.59)
i2 = Item("jeans", 30, 44.99)
i3 = Item("shirt", 20, 29.99)

print("{:<10} {:<10} {:<10} {:<10}".format("Item", "Cost", "Price", "Extra Info"))
print("-" * 60)
print("{:<10} {:<10.2f} {:<10.2f} ".format(i1.name, i1.cost, i1.price))
print("{:<10} {:<10.2f} {:<10.2f} ".format(i2.name, i2.cost, i2.price))
print("{:<10} {:<10.2f} {:<10.2f} ".format(i3.name, i3.cost, i3.price))
print("-" * 60)

# Create Clothing and Food items and print them
c1 = Clothing("jeans", 30, 44.99, "Levis", 32)
c2 = Clothing("shirt", 20, 29.99, "Macy's", 16)
f1 = Food("bananas", 2.00, 4.59)
f2 = Food("Avocado", 1.50, 5.50)
f2.shelf_Life = 2

print(c1)
print(c2)
print(f1)
print(f2)
print("-" * 60)

# Create Shoes and Chips and print them
s1 = Shoe(59.99, 89.99, 10)
s2 = Shoe(49.99, 79.99, 4)
h1 = Chips()

print(s1)
print(s2)
print(h1)
print("-" * 60)

# Testing out the range checking
h1.shelf_Life = -5
s2.size = -2

print(s2)
print(h1)
print("-" * 60)

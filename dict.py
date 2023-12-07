#we will create a dictinoary also called Hash table and iterate over it.
my_menu = {
  'sushi' : {
    'price' : 19.25,
    'best_served' : 'cold'
  },
  'paella' : {
    'price' : 15,
    'best_served' : 'hot'
  },
  'samosa' : {
    'price' : 14,
    'best_served' : 'hot'
  },
  'gazpacho' : {
    'price' : 8,
    'best_served' : 'cold'
  }
}

# Iterate the elements of the menu
for dish, values in my_menu.items():
  # Print whether the dish must be served cold or hot. .title() method will make the key which is dish start with capital letter.
  print(f"{dish.title()} is best served {values['best_served']}.")
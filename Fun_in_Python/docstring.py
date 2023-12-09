import inspect

def build_tooltip(function):
    """
    The `build_tooltip` function takes a function as an argument and returns a formatted tooltip string
    containing the docstring of the function.
    @param function - The "function" parameter is the function for which we want to build a tooltip.
    @returns The function `build_tooltip` returns a string that consists of a border made of "#"
    characters, followed by the docstring of the input function, and then another border made of "#"
    characters.
    """
  
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
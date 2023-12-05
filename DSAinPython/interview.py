import math
def my_zip(*args):
    
    # Retrieve Iterable lengths and find the minimal length
    lengths = list(map(len, args))
    min_length = min(lengths)

    tuple_list = []
    for i in range(0, min_length):
        # Map the elements in args with the same index i
        mapping = map(lambda x: x[i], args)
        # Convert the mapping and append it to tuple_list
        tuple_list.append(tuple(mapping))

    return tuple_list

result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
print(result)

# Exclude all the numbers from nums divisible by 3 or 5
print(nums)
fnums = filter(lambda x: x%3 !=0 and x%5 !=0, nums)
print(list(fnums))

# Return the string without its vowels
print(string)
vowels = 'aeiou'
fstring = filter(lambda x: x.lower() not in vowels, string)
print(''.join(fstring))


# Filter all the spells in spells with more than two 'a's
print(spells)
fspells = filter(lambda x: x.count('a')>2, spells)
print(list(fspells))

# Convert a number sequence into a single number
nums = [5, 6, 0, 1]
num = reduce(lambda x,y: x*10+y, nums)
print(str(nums) + ' is converted to ' + str(num))

# Find common items shared among all the sets in sets
sets = [{1, 4, 8, 9}, {2, 4, 6, 9, 10, 8}, {9, 0, 1, 2, 4}]
common_items = reduce(lambda x,y: x.intersection(y), sets )
print('common items = ' + str(common_items))

# Reverse a string using reduce()
string = 'DataCamp'
inv_string = reduce(lambda x,y: y+x, string)
print('Inverted string = ' + inv_string)


def fib(n):
  if n < 2:
    return (n, 1)

  fib1 = fib(n-1)
  fib2 = fib(n-2)

  return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)
  
  
# Calculate an average value of the sequence of numbers
def average(nums):
  
    # Base case
    if len(nums) == 1:  
        return nums[0]
    
    # Recursive call
    n = len(nums)
    return (nums[0] + (n-1) * average(nums[1:])) / n

# Testing the function
print(average([1, 2, 3, 4, 5]))

def average(nums):
    result = 0
    for num in nums:
        result += num
    return result/len(nums)
    
# Write an expression to get the k-th element of the series 
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    
    # Define the base case 
    if n == 0:
    	return 4
    # Recursively calculate pi
    # Make the recursive call
    return 4 * curr_elmnt + calc_pi(n-1)
  
# Compare the approximated Pi value to the theoretical one
print("approx = {}, theor = {}".format(calc_pi(500), math.pi))


'''This solution works by iterating over the 2D numpy array (or matrix) in a spiral pattern and converting each part of the spiral into a list.

Here's how it works:

The outer loop for i in range(0, size): iterates over the matrix from the outermost layer to the innermost layer. The variable i represents the current layer.

The first line inside the loop, spiral += list(square[i, i:size-i]), selects the top row of the current layer (marked by a red arrow) and converts it into a list. The slicing operation square[i, i:size-i] selects all elements from the ith row, starting from the ith column to the (size-i)th column.

The second line, spiral += list(square[i+1:size-i, size-i-1]), selects the right column of the current layer (marked by a green arrow) and converts it into a list. The slicing operation square[i+1:size-i, size-i-1] selects all elements from the (i+1)th row to the (size-i)th row in the (size-i-1)th column.

The third line, spiral += list(reversed(square[size-i-1, i:size-i-1])), selects the bottom row of the current layer (marked by a blue arrow), reverses it, and converts it into a list. The slicing operation square[size-i-1, i:size-i-1] selects all elements from the (size-i-1)th row, starting from the ith column to the (size-i-1)th column.

The fourth line, spiral += list(reversed(square[i+1:size-i-1, i])), selects the left column of the current layer (marked by a magenta arrow), reverses it, and converts it into a list. The slicing operation square[i+1:size-i-1, i] selects all elements from the (i+1)th row to the (size-i-1)th row in the ith column.

The += operator is used to append each list to the spiral list.

By the end of the loop, the spiral list contains all elements of the matrix in a'
'''
spiral = []

for i in range(0, size):
    # Convert each part marked by a red arrow to a list
    spiral += list(square[i, i:size-i])
    # Convert each part marked by a green arrow to a list
    spiral += list(square[i+1:size-i, size-i-1])
    # Convert each part marked by a blue arrow to a list
    spiral += list(reversed(square[size-i-1, i:size-i-1]))
    # Convert each part marked by a magenta arrow to a list
    spiral += list(reversed(square[i+1:size-i-1, i]))
        
print(spiral)

 # Substitute the code in the block 1 given the input_array1
output_array1 = input_array1*5
print(list(map(lambda x: [5*i for i in x], input_list1)))
print(output_array1)

# Substitute the code in the block 2 given the input_array2
output_array2 = input_array2[input_array2 % 2 ==0]
print(list(filter(lambda x: x % 2 == 0, input_list2)))
print(output_array2)

# Substitute the code in the block 3 given the input_array3
output_array3 = input_array3**2
print([[i*i for i in j] for j in input_list3])
print(output_array3)

def prevalence(series):
    vals = list(series)
    # Create a tuple list with unique items and their counts
    itms = [(x, vals.count(x)) for x in set(vals)]
    # Extract a tuple with the highest counts using reduce()
    res = reduce(lambda x, y: x if x[1] > y[1] else y, itms)
    # Return the item with the highest counts
    return res[0]

# Apply the prevalence function on the scores DataFrame -- mode() function can also be applied.
result = scores[groups_to_consider].apply(prevalence)
print(result)

def rank(series):
    # Calculate the mean of the input series
    mean = np.mean(series)
    # Return the mean and its rank as a list
    if mean>90:
        return [mean,'high']
    if 60< mean <=90:
        return [mean, 'medium']
    return [mean, 'low']

# Insert the output of rank() into new columns of scores
cols = ['math score', 'reading score', 'writing score']
scores[['mean', 'rank']] = scores[cols].apply(rank, axis=1, result_type='expand')
print(scores[['mean', 'rank']].head())

def rescale(series, low, high):
   # Define the expression to rescale input series
   return series * (high-low)/100 +low

# Rescale the data in cols to lie between 1 and 10
cols = ['math score', 'reading score', 'writing score'] 
scores[cols] = scores[cols].apply(rescale, args=[1,10])
print(scores[cols].head())

# Redefine the function to accept keyword arguments
def rescale(series, low=0, high=100):
   return series * (high - low)/100 + low

# Rescale the data in cols to lie between 1 and 10
cols = ['math score', 'reading score', 'writing score']
scores[cols] = scores[cols].apply(rescale, args=[1,10])
print(scores[cols].head())

import numpy as np

# Group the data by two factors specified in the context
groups = heroes.groupby(['Alignment', 'Publisher'])

# Filter groups having more than 10 valid bmi observations
fheroes = groups.filter(lambda x: x['bmi'].count()>10)

# Group the filtered data again by the same factors
fgroups = fheroes.groupby(['Publisher','Alignment'])

# Calculate the mean and standard deviation of the BMI index
result = fgroups['bmi'].agg([np.mean, np.std])
print(result)

'''NaN value imputation
Let's try to impute some values, using the .transform() method. In the previous task you created a DataFrame fheroes where all the groups with insufficient amount of bmi observations were removed. Our bmi column has a lot of missing values (NaNs) though. Given two copies of the fheroes DataFrame (imp_globmean and imp_grpmean), your task is to impute the NaNs in the bmi column with the overall mean value and with the mean value per group defined by Publisher and Alignment factors, respectively.

Tip: pandas Series and NumPy arrays have a special .fillna() method which substitutes all the encountered NaNs with a value specified as an argument.'''
# Define a lambda function that imputes NaN values in series
impute = lambda series: series.fillna(np.mean(series))

# Impute NaNs in the bmi column of imp_globmean
imp_globmean['bmi'] = imp_globmean['bmi'].transform(impute)
print("Global mean = " + str(fheroes['bmi'].mean()) + "\n")

groups = imp_grpmean.groupby(['Publisher', 'Alignment'])

# Impute NaNs in the bmi column of imp_grpmean
imp_grpmean['bmi'] = groups['bmi'].transform(impute)
print(groups['bmi'].mean())

# MAP
# Map function is used to iterate a function in a list.
# It's syntax => map(function_name, iterable)
# Suppose, we have a list and we want a new list where the original elements are tripled
def trip(x) : 
    x = x * 3 
    return x
a = [1, 4, 2, 3, 10]
print(list(map(trip, a)))

# Make sure you add 'list()' in the above statement to get the desired output. You can even use 'tuple()' or any other function to change the data type

# FILTER 
# filter() is used to filter elements and turn them into list
def fil(x) : 
    if x > 2 : 
        return x 
    else : 
        pass 

b = filter(fil, a)
print(list(b))

# REDUCE 
# reduce() is used to join all the elements together
# Let's understand how this works
# To get reduce function, you need to import a module called 'functools'
from functools import reduce
def s(x, y) : 
    return x+y

c = [2, 3, 6, 10, 5, 1]     # We create a list
d = reduce(s, c)
print(d)

# Now the python will calculate its sum 
# Step 1 - c = [5, 6, 10, 5, 1], it will add up first two elements of a list
# Step 2 - c = [11, 10, 5, 1]
# Step 3 - c = [21, 5, 1]
# Step 4 - c = [26, 1]
# Step 5 - c = [27]     <-- This will be the output
# Thus, this is the flow of execution

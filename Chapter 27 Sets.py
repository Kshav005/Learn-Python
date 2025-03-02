# Set is a collection of well defined objects
# It doesn't allow multiple entries with same element
# So it is useful to use this data type for various jobs
# Set is easy to create, just like lists and tuples

# We create a set by using curly brackets '{}'
s = {"hello", 2, 3, 4, 5, 6, 2, 2, 3}
print(s)    # It will not print the repeated values

# It doesn't not maintain order!
# It is seperated by commas
# They are unchangeable (immutable)

# It can have any data tpe 
se = {"hi", 34.2, 3, True}


# To print all the elements of a set, use for loop
for i in s : 
    print(i)    # Prints in random order
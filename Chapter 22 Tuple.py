# Tuple is a type of list but not completely list. It is very useful in various fields of computer programming.
# Tuples are immutable which means, we cannot change the elements of a tuple
# A tuple starts with circle brackets '()' and seperated with commans ','

t = (3, 35, 23, "There", "No")

# To show a single element tuple, end it with a comma otherwise Python will interpret it as an integer
y = (4,)

# Though, you can print the elements using the index feature
print(t[-1])
print(t[2])

# We can check for an element also, just like we did in list
if 23 in t : 
    print("Yes, it is present")
else : 
    print("Nothing here.")
    
# We can use slicing in tuple as well
print(t[1 : -1 : 2])


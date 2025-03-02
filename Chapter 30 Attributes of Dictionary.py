# There are various methods to manipulate your dictionary

a1 = {2 : "Hi", 3 : "Bye", 3 : 34}
a2 = {8 : 23, 5 : "Three", 23 : "Why", 55 : 93}
a3 = {32 : 11, 45 : 232}

# To merge and update the original dictionary 
a1.update(a2)

# To clear all the elements from a dictionary
a1.clear()

# To remove a pair '.pop("key_here")
a2.pop(23)

# To remove the last element
a2.popitem()

# To delete the whole dictionary
del a3
del a2[8]   # Will delete the element if key provided otherwise deletes the whole dictionary




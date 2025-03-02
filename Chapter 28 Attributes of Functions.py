# We can use various methods to manipulate sets in python
# Sets in python are same as the mathematical sets

s1 = {4, 3, 2, "There", "Nothing"}
s2 = {3, 2, 12, 34, "Where"}
s3 = {1, 1, True, 12, 3}
s4 = {1, True, 1}
s5 = {None, 3, 324}

# Joining two given sets (UNION OF SETS)
print(s1.union(s2))

# To update/merge elements from other set permanently
s1.update(s2)
print(s1)

# To get two common elements in both sets (INTERSECTION)
print(s1.intersection(s3))

# To get the set where all common elements are removed (SYMMETRIC DIFFERENCE)
print(s2.symmetric_difference(s3))

# To check if elements of a set is available in another set (gives False if present)
print(s1.isdisjoint(s3))

# To check if all elements of a set is part of another set (gives True if present)
print(s2.issuperset(s3))

# To check if all elements of a set can be part of another set in another set
print(s4.issubset(s3))

# To add elements 
s2.add("Meow")
print(s2)

# To remove elements
s2.remove("Meow")   # using this will throw an error if item not present
s2.discard("THe")   # using this will not throw error if item not present

# To remove the last element of the set
s3.pop()    # As the sets are unordered, it is not known that which element will get removed

# To delete entire set 
del s4 

# To delete entire elements of a set
s1.clear()


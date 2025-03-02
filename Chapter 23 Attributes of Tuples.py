# We cannot manipulate a tuple, which means we cannot add or remove any element
# To change elements, we can convert the tuple into list, then add an element and then turn it back to a tuple.
t = (3, 5, 23, 233, 54, 12, 675, 230)
a = list(t)
a.append("Russia")
print(a)
t = tuple(a)
print(t)

# We can merge two tuples also
b = ("India", "USA", "Blaze")
c = t+b
print(c)

# We can count elements in a tuple 
res = ("2", 5, 23, 122, 1, "There", "Nice", 3, 5, 122, 23, 5)
print(res.count(5))

# To get the index of a particular element
print(res.index(23))

# To get the length of list/tuple 
print(len(res))
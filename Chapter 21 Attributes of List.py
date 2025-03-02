# Lists have many inbuilt attributes
# Suppose if we want to find a certain number in the list
a = [2,3,4,33,63,21,65,12]
c = ["J", "the", "hero", "pray", 45]
b = 0
if 6 in a :
    print("Present")
else : 
    print("Not present")    # Same thing can be applied in string indexing also
    
# Printing elements of lists to certain length [start : end : step]
print(a[2:])    # If end is kept blank then its default value will be till the last element of the list

# Using step in list
print(a[1:-1:2])

# Adding an element at the end of a list
a.append(78)
print(a)

# Sorting the elements 
a.sort()
print(a)

# Sorting the elements in reverse order
a.sort(reverse=True)
print(a)

# Reversing the elements of a list
c.reverse()
print(c)

# To get the index of an element (first occurence only)
print(c.index("the"))

# To count the number of occurences in list
print(c.count("J"))

# To copy the list 
d3 = a.copy()
print(d3)

# To insert element to a specific index, .insert(index, element)
c.insert(5, "Where")
print(c)

# To extend a list (merging two lists)
li = [3, 2, 53, 23, "There"]
a.extend(li)
print(a)

# We can merge two lists by another way also (this will create another list with all elements of both the lists)
y = li + a
print(y)

# Deleting an element from a certain index
a.pop(3)
print(a)

# Removing an element using element name
a.remove(12)
print(a)

# Enumerate function is a built in function and can save time!
# It is used to get index of an element easily!

a = ["Zero", "One", "Two", "Three", "Four"]

for i, x in enumerate(a) : 
    print(f"'{x}' is in index {i}")
    
# Using this function can solve various problems and can help you to know which element is on which position
# To change the starting index

for p, q in enumerate(a, start=2) :     # It will print the elements starting from index 2
    print(p, q)

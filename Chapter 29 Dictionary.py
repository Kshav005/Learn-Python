# Another important concept in Python is Dictionary
# Dictionary contains key-value pair
# It can be used to store values, or to create a mapping
# Create a dictionary by using curly brackets '{}' and colon ':'
# {key : value}
a = {"Meow" : "Sound of Cat", 
     "Paper" : "A white sheet, created by Trees",
     "Tree" : "Living organism, which gives out oxygen"}

# To get the value of a key (2 methods)
print(a["Meow"])        # Will throw error if key not present
print(a.get("Tree"))    # Will not throw error if key not present

# To get all the values of keys 
print(a.values())

# To get all the keys of values
print(a.keys())

# To print all the keys/values, one by one
for i in a.keys() : 
    print(i)
    
# To get all the key-value pairs 
print(a.items())

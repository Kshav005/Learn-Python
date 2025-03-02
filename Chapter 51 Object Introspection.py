# dir()
# The dir() returns the a list of all the attributes and methods existing in a module
import time 
print(dir(time))

a = [1, 4, 6]
print(dir(time))        # This will show how many methods we can use on a list! It will consist of 'reverse', 'sort' and many more


#__dict__()
# This returns a dictionary representation of an object's attribute
class Driver : 
    def __init__(self, name, age) : 
        self.name = name 
        self.age = age 
    
b = Driver("XyZ", "32")
print(b.__dict__)            # This will return the dictionary where key is the variable and the value is the value assigned to that variable.


# help
# help() tells about everything regarding a class
print(help(int))
print(help(time.sleep))


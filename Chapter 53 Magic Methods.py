# Magic methods are also known as Dunder methods, and they start/end with double score'__'
# They have special purposes and that's why they are called magic
# To improve skills in OOP then you should check out this chapter definitely.


# __len__
class Name : 
    def __init__(self, name) :
        self.name = name
    def __len__(self) : 
        i = 0 
        for x in self.name : 
            i = i + 1 
        return i

a = Name("ABCDEFGH")
print(len(a))           # We needn't use underscore for the use 


# __init__ 
# We have already seen this, it is used to set up object's initial state
class ABC : 
    def __init__(self, user) :
        self.user = user


# __call__
# It is used to make an object callable 

class Shop : 
    def __init__(self, sname) :
        self.sname = sname
    def __call__(self) :
        print("I am being called")
    
a = Shop("Jerry")
a()             # We can now get make the object callable and we get the desired result
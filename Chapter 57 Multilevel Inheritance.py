# Multilevel inheritance is the child's child of the parent's class

class Greet :
    pass 

class Hello(Greet) : 
    pass 

class Hi(Hello) : 
    pass


# There is another type of inheritance called Hierachy Inheritance
# In this inheritance, the parent class has 2 or more child class
class Where : 
    pass 

class Here(Where) : 
    pass 

class There(Where) : 
    pass


# There is one more inheritance known as hybrid inheritance
# It is a mixture of all the inheritances

class Clothes :             # This is simple inheritance
    pass

class Shirt(Clothes) :      # This is Hierachy Inheritance
    pass 

class Pant(Clothes) :       # Part of Hierachy Inheritance, can be also Multilevel Inheritance
    pass 

class Fashion(Shirt, Pant) : # Multiple Inheritance
    pass



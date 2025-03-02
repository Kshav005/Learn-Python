# Access specifiers or modifiers in python is used to limit the access of class variables outside, when an object is created
# There are 3 types of access modifiers : Public Access Modifiers, Private Access Modifiers and Protected Access Modifiers
# There is no such existing thing in Python but people use it as a convention. Python doesn't enfore any of it.

# PUBLIC ACCESS MODIFIERS
class world :
    def __init__(self, city_name, country_name) :
        self.ciname = city_name         # Public Variable
        self.coname = country_name      # Public Variable
    def show(self) : 
        print(f"The city {self.ciname} is situated in {self.coname}")
        
a = world("New York", "USA")
a.show()
print(a.ciname)     # Thus we can access these variables


# PRIVATE ACCESS MODIFIERS
class Employee : 
    def __init__(self, name, e_id) :
        self.__name = "Mark"     # If we add '__' in the starting of a variable then it will become private variable
        self.id = e_id         
    
a = Employee("Warner", "23")
print(a.__name)     # And thus you can't access it directly
print(a._Employee__name)        # But it can be accessed indirectly
# This is known as name mangling, it is a technique to protect class private attributes


# PROTECTED ACCESS MODIFIERS
# This is not much important to check this but the variable is prefixed with a single underscore (_) here.
# It's not mentioned by Python that it will provide any restriction or protection.
class Pen : 
    def __init__(self, name) :
        self._name = name 
    
a = Pen("Octane")
print(a._name)    
    
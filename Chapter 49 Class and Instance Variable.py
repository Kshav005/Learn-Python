# Now we are going to check up a little on the difference between class and instance variables
class Car : 
    garage_name = "Callahan Garages"    # This is class variable
    def __init__(self, cname, cid) :
        self.cname = cname      # This is instance variable
        self.cid = cid          # This is instance variable
    def show(self) : 
        print(f"The car with id {self.cid} is {self.cname}!")

a = Car("Audi R8", "3443")

a.show()        
Car.show(a)     # This will yield the same output as the above code

a.cid = "2343"  # You can change instance variables like this
a.show()   
        
        
# Class variable is common for every instance (fuctions created in class) while instance variables are just for specific instances. This concept is same as global and local variables.        
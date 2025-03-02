# Super keyword is used to call child class from a parent class
class Parent : 
    def parent_instance(self) : 
        print("This is parent function!")

class Child(Parent) : 
    def child_instance(self) : 
        print("This is child instance!")
        super().parent_instance()           # We use 'super' to specify the instance of the parent class
        
child = Child()
child.child_instance()      # And we got both parent and child instance outputs

# super() is used to define an instance from the parent class when there is no such instance with the name in child class.
# We can also use it to inherit the variables from parent class too!
class Office : 
    def __init__(self, name, loc) :
        self.name = name
        self.location = loc
    def hello(self) : 
        print(f"Hello, employee from {self.name}")
    
class Branch(Office) : 
    def __init__(self, name, loc):
        super().__init__(name, loc)     # Inheriting the variables from the parent class

a = Branch("Brendon Offices", "USA")        
a.hello()


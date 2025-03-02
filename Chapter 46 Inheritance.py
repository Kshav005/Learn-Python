# Inheritance is a way to use existing class to extend another class

# Creating a class 
class Car : 
    def __init__(self, cname, cnum) :
        self.cname = cname
        self.cnum = cnum 

    # Creating a function
    def detail(self) :          
        print(f"The model of the car is {self.cname} and number plate is {self.cnum}")
    
a = Car("Ford GT", "DF3729")
a.detail()
b = Car("Mercedes Benz", "JT3211")
b.detail()

# To inherit from old class 
class year(Car) : 
    def driver_name() : 
        print("The driver name is not entered")

# And now you can make object with class name also!
c = year("Golf GTI", "TP1242")
c.detail()

# You can make more inheritances and make your code efficient and clean


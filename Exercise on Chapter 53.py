# In this exercise, you have to make a class 'Vehicle' and print the information of the vehicle if the object is called.
# Good luck! Below is the solution 









class Vehicle : 
    def __init__(self, mode, transport) :
        self.mode = mode 
        self.transport = transport
    def __call__(self) :
         print(f"The {self.transport} mode is {self.mode}.")

a = Vehicle("Airways", "Aeroplace")
a()

# Hence, the exercise is complete!

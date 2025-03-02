# OOP (Object Oriented Programming) is a very complicated thing.
# It uses classes and objects to work efficiently.
# The regular old programming we did before this chapter is known as Procedural Programming.
# OOPs is used to represent real-world concepts and hence it becomes important for us to learn this!
# A 'class' is a brueprint which stores information that is needed to be provided everytime
# An 'object' is an instance and it has its own data. It is property of class.

# Suppose, we are creating a game where our main character will be hunt down by 20 enemies having guns
# Now, if we use Procedural Programming then we will have to create multiple variables to store health and guns that they will hold.
# But if we use OOP, then it will be way too easier to do so, as we will create a blueprint already and we just need to assign them to different enemies

# We can create class by using keyword 'class'
class House : 
    hname = "Grand Plaza"
    hnum = "23"
    
    
# Now to change details
a = House()             # This is an object, used to access elements  
a.hname = "Great Home"
a.hnum = "45"
print(a.hname, a.hnum)

# We can create more objects 
b = House()
b.hname = "All House Plans"
b.hnum = "19"
print(b.hnum, b.hname)

# A class can also have a funtion!
class Cars : 
    cname = "Mercedes"
    
    def info(self) : 
        print(f"The car is {self.cname}")       # self is a function which is used to select the variables for the object that you have created. Thus, you will get different outputs for different values passed in object
        
c = Cars()
c.cname = "Audi"
d = Cars()
d.dname = "Supra"
c.info()
d.info()

# Thus we are getting two different outputs in the above code!
# By this way, we can create any number of enemies, just by passing default values in class and creating numerous functions



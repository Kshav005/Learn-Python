# Constructors are used in initialising while creating objects.
# The old way to use OOP that we learnt in the previous chapter 
class school : 
    name = "World School"
    highest_class = "12th"
    def abc(self) :         # Using self is must, make it a habit
        print(f"The school name is {self.name} and the highest class is {self.highest_class}")
a = school()
a.name = "Globe School"
a.highest_class = "5th"
a.abc()

# The new way using constructor is given below 
class university : 
    def __init__(self, cname, course):         # '__init__' will be run automatically as soon an object has been created!
        self.cname = cname
        self.course = course
        
    def info(self) : 
        print(f"The {self.cname} provides {self.course} courses")

a = university("KJM University", "13")
b = university("JKT University", "20")
c = university("ABC University", "50")

a.info()
b.info()
c.info()

# And this will work just fine.
# But don't forget, self is an argument which is taken automatically. So you needn't enter any argument for it.
# There is another type of constructor which is known as default constructor. It doesn't take any arguments
class Magic : 
    def __init__(self) :
        print("There is a cat!")
obj1 = Magic()
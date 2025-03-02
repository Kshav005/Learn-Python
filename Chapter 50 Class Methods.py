# In earlier chapters, we learn that to create custom classes, we use 'class'
# Now, we are going to learn about methods to manipulate class
# We can use '@classmethod' decorator to change a class variable permenantly

class school : 
    sname = "Global Internation School"
    def show(self) : 
        print(f"{self.name} studies in {self.sname}")
    
a = school()
a.name = "ABC"
a.sname = "World School"
a.show()
print(school.sname)              # So you can see, the class variable didn't change permanently

# To change that 
class ecom : 
    name = "Amazon"
    def info(self) : 
        print(f"I work in {self.name}")
    
    @classmethod
    def change(cls, newname) :      # 'cls' is a class which is passed as an argument automatically
        cls.name = newname
        
b = ecom()
b.change("ebay")
print(ecom.name)        # And now you can see the difference here!




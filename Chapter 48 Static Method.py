# Static method belongs to a class rather than an instance of class.
# They are created using '@staticmethod' decorator and do not have access to 'self'.

class Maths : 
    def add(self, num1, num2) :     # The normal way to make function 
        num1 = num1 + num2 
        print(num1)
    
    @staticmethod
    def sub(a, b) : 
        print(a-b)
    
a = Maths()
a.add(6, 6)             # Here we are using object variable to get the desired results
Maths.sub(5, 3)         # Therefore, we can access the static function just by using the class name and not the object variable

# You can use static method to remove the difficulty of using 'self'
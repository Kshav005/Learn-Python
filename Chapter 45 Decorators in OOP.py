# Decorators are a powerful way to modify the behaviour of a function. They are used to enhance the functionality of a function
# Decorators can be applied by using '@'
# Suppose we want to say 'Hello user' before every function.
# It wouldn't be easy because you will have to copy paste this, if you have nearly 50 functions or more
# So, to solve this problem, we use the decorators

def hello(ab) :         # This function will take a function as an argument
    def fx() :
        print("Hello user")
        ab()
    return fx

@hello              # Using '@' to depict that the decorator is 'hello' function
def abc() : 
    print("There is not a cat")

abc()


# But there is a different approach to use functions with arguments. Such as a function which takes two numbers and adds them.
def meow(x) : 
    def mi(*args, **kwargs) :              # You need to add '*args' and *kwargs' ass parameters in this function
        print("MEOW")
        x(*args, **kwargs)                 # Using those parameters as arguments to perform the function
    return mi

@meow 
def add(a, b) : 
    print(a+b)

add(5, 6)
    
# '*args' is used to take the arguments as tuple 
# While '**kwargs' is used to take arguments as dictionary




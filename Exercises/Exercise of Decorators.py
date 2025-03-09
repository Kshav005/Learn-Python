# In this exercise, you need to create a authenticator decorator, argument decorator, timer decorator and a non argument decorator. Authenticator decorator is just a decorator which runs a function which is must before any function, for example, check if user is already registered or something like that. Needn't exactly to look into a registered user in this exercise but it should be checking what needs to be checked.


















# Non argument decorator
def default(func) :
    def wrapper() :
        print("Executing.....")
        func()
    return wrapper

@default
def fun1() :
    print("Success")
    
# ARGUMENT DECORATOR
def checkArgument(func) :
    def wrapper(*args, **kwargs):
        print("Executing.....")
        func(*args, **kwargs)
    return wrapper

@checkArgument
def fun2(a) :
    print("Hey", a)    
    
    
# CHECKING DECORATOR
def checks(func) :
    def wrapper(carName):
        cars = ["Audi", "BMW"]
        func(carName)
        if carName not in cars :
            print("This was not in the list!")
        else :
            print("Found it!") 
    return wrapper

@checks
def fun3(car) :
    print("Hey", car)    

fun3("j")
fun3("Audi")


# Congrats on completing this exercise! Good luck on your practice.
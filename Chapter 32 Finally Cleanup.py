# With try and except, there is a new keyword used with it.
# Suppose we want our code to run irrespective of situations

try : 
    l = ["he", 5, 4, 12]
    print(l)
    a = input("Enter index to print from the list : ")
    print(l[a])
except : 
    print("Something went wrong")
    
print("Here I am running!")

# The above code will run perfectly even without using the keyword
# But the main problem will be caused during function making
def new(b) : 
    try : 
        return int(b)
    except : 
        return "It's not a number, brother"
    print("This time, I will not run hehe")
    
print(new(3))

# But if we use 'finally', then 
def new2(c) : 
    try : 
        return int(c)
    except : 
        return "I am hero"
    finally : 
        print("There is a cat")
print(new2(5))

# This time, the last statement in function will be printed, after using 'return' the code doesn't run other codes return after it
# But you can make those codes run by using 'finally' and it will force python to run that statement

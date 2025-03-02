# Functions are an efficient way to organize codes!
# Developers use this to ensure proper management of codes
# A function consists of keyword 'def', function name, colon, paranthesis (brackets), parameters and working code.

def plus(a, b) :        # We are taking two numbers from the user, which will get assigned to variables 'a' and 'b' respectively
    c = a + b           # Indentation (Spacing) is required to represent the block of code
    print(c)

plus(7, 5)      # This is a way to call a function, which means if we use the function_name(value, value) here then it will run the code by assigning those numbers into the variable

# It is not necessary for a function to accept arguments, it depends on the developer
# Creating a greater than function
def greaterthan(a,  b) :    # Try to understand the function
    if a > b :          
        print(a, "is greater than", b)
    elif a < b : 
        print(b, "is greater than", a)
    else : 
        print("Both numbers are equal")
        
# Asking user to input two numbers
c1 = input("Enter a number : ")     
c2 = input("Enter another number : ")

# Changing the variables to integers
c1 = int(c1)
c2 = int(c2)

# Calling the function
greaterthan(c1, c2)     


# Functions will also lessen the number of code lines as a certain command will not be repeated again and again
# There is a keyword called 'pass' which is used as "Nothing here" in fuctions

def abc() : 
    pass 

abc()       # If we call this function then it will print nothing.

# 'pass' is an advantage for developers to avoid errors and can test other lines of codes and they can make the funtion later on.

# There are 3 types of functions : 
# 1. User-defined function - The function which is created by you, a user. Like the above one was created by us.
# 2. Built-in functions - The functions which are already present in python. For example - print(), list(), int()
# 3. Module functions - The functions which are only present in modules. For example - strftime() is a function when we import time module




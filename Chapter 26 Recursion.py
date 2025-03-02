# Recursion is defined as calling the function itself in a function.
# It is complicated but helpful in creating series like Fibonacci and Arithmetic, etc

# Creating a factorial function
# Factorial is "a x a-1 x a-2 x a-3 x a-4 ..... x 1"
# factorial(5) = 5 x 4 x 3 x 2 x 1
# factorial(6) = 6 x 5 x 4 x 3 x 2 x 1

def factorial(a) : 
    if a == 1 or a == 0 : 
        return 1
    return a*factorial(a-1)     # return is used to store a value, which means we need to use print(function_call) to get the output

print(factorial(5))

# Recursion is just all about calling the function itself again!
# Creating a range type function
def mess(c) :
    if c != 0 : 
        c = c - 1
        print("Hello there")
        mess(c)
    elif c == 0 :     # variable defined in function is known as local variable
        print("Done")
b1 = int(input("How many times should it be printed?"))     # the variable outside function is global variable
mess(b1)     # Same global and local variables can exist!

# Creating a Fibonacci Series
def fibo(a) : 
    if a == 0 : 
        return 0
    return a + fibo(a-1)
print(fibo(4))

# Above are some examples of recursion, hope you understood the concept!
# Lambda is an expression to create functions in just one line of code

def pr(x) : 
    x = x * 5
    return x 
print(pr(4))

# The above is a function which covers nearly 3 lines
# But the same can be done by using lambda

br = lambda x : x * 5
# The above line states that a function named 'br' is created and then lambda is used to tell that the function will take a variable 'x' and then it will multiply that variable to 5
# It will automatically return the value

print(br(4))

# Lambda functions are cool to use if you want to create short functions numerous times.
# Otherwise the normal way to create a function is used as it is more readable
# Lambda functions are not suitable for creation of complex functions.

# It can also take multiple variables!
avg = lambda x,y,z : int((x+y+z)/3)
print(avg(1,3,5))


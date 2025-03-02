# There are many types of arguments in functions of python
# Default Arguments - 
def plus(a = 9, b = 1) :    # By default the value of variables will be 9 and 1 if the user doesn't pass any value while calling the function
    print(a+b)

# Calling the function
plus(3, 6)  # with arguments
plus()      # without arguments, it will take the value as 9 and 1
plus(5)     # passing the value of 'a' only, then python will take the default value of 'b'
plus(b = 7) # passing the value of 'b' only 

# 2. Required Arguments - 
def minus(a, b=6) :     # Here the 'a' is required argument as there is no default value given
    print(a-b)

minus(5)        # If value of 'a' is not given then the program will not run and will throw an error
    
# 3. Variable length Arguments - 
# We can add unlimited variables too
def add(*ty) :
    y6 = 0
    for i in ty : 
        y6 = y6 + i
    print(y6)

add(1,2,3,4,5,6,7,8,9,10)   # Adds all the numbers passed in the function call
        
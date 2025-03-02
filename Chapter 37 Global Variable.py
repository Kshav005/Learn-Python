# In the previous chaptes, it was explained that there are two types of variables
# To revise, one is function defined variables and other is the normal variable
# Function defined variables are known as local variables while outside the function (normal) variables are known as global variables

# Some examples of global variables-
a = 34
b = "Three"
c = None 
d5 = True 
erierhno = False 
e_jrl = "pray"

def nothing() : 
    
# Some examples of local variables
    a = 32
    b = 23
    c = True
    d = "Yes"
    
# It means if we try to change variable values within a function then it will not change the value of global function 
you = 34

def there() : 
    you = 76
    return you
print(there())
print(you)


# After running the above code, you can see that we are getting two different values of variable "You". This clears the idea of global and local Variables
# To alter the values of a variable, we can use the keyword 'global variable_name'!
u = 45
def here() : 
    global u 
    u = 56
    return u
print(here())
print(u)

# Now as you can see, after running the code, the value of variable 'u' gets changed!
# That is how you can control the value of a global variable even being inside a function

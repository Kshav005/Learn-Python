# The main aim to create a custom error is to stop the program from creating further mess.
 
a = int(input("Enter a number : "))
if a < 500 or a > 900 : 
    raise ValueError("Number should be between 500 to 900")

# 'raise' is used to stop the code from running any further by showing desired error
# This will not complicate the next line of code
# We can also name our own errors by using classes of Python
# Class will be taught in further chapters


# To save your code from crashing upon error, we can use error handling
# It is a cool concept to save your API from stopping if an error occurs

a = input("Enter a number : ")

# Now to avoid error if the user added some string instead of number
try : 
    print(int(a)-5)                  # The calculation will not happen if the input value will be string 
except :         # If some error occurs 
    print("You didn't enter a valid number :(")
    

# We can also handle specific errors but you need to learn all types of errors in python
# Infinite number of 'except's can be used
b = input("Enter number one more time - ")
try : 
    print(int(b))   
except ValueError : 
    print("It's not an integer!")
    
except IndentationError : 
    print("Oops, something went wrong!") 
    
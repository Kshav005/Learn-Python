# Now it's the time to learn about while loops!
# While loops are a bit complicated than for loops
# But while loops are mostly used in complex codes and not in number related stuff.

for i in range(0,6) : 
    print(i)        
    
b = 0    
while b < 6 :
    print(b)
    b = b + 1
    
# Both the above codes work the same but as you can see, the while loop code is lengthy and a little hard to understand

# So the while loop is very useful in other ways
while b < 30 : 
    input("Enter a word : ")
    
# The above code will run will ask for output from the user until the variable 'b' becomes equal to 30


# Python will run the while loop code until the condition becomes False
# The while loop becomes stronger than for loop when we have to print the numbers in reverse order which is very complex using for loop.
c = 10 
while c > 0 : 
    print(c)
    c = c - 1
    
# But make sure you avoid errors while using this type of loop because if one error occurs in terms of calculation then the code will run infinitely!
# We can also use 'else' in loops! 
nume = 0
while nume <= 10 : 
    print(nume)
    nume = nume + 1
else : 
    print("The number is now greater than 10!")
    print(nume)


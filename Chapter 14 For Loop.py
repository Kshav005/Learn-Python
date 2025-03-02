# Today we are going to learn about 'loops'. 
# Loops are very important and are useful as well!
# There are two types of loop - 'for' and 'while'.
# Let's find out what each type of loop contains!
# Suppose we want to print numbers from 1 to 10
# So we are going to use 'for loop' by using keyword 'for'
# Syntax - for variable in range(start, end)
# The "variable" will be assigned all the values one by one from the range

for i in range(1,10) : 
    print(i)
    
# In range, the start will be inclusive but not the end number.
    
# To print all the charaters in a string
a = "Nevermind"
for b in a : 
    print(b)        # The variable 'b' will get assigned with the character one by one from the variable 'b' and then it will print them out in sequence
 
 
# We can also use conditions in loop!
a3 = "Noodles"
for c in a3 : 
    print(c)
    if c == "l" : 
        print("L is for Lion!")     # This part of code will work only when the variable c would be equal to 'l' in the string
        

# Step in Loops
# Step is skipping numbers while printing the output
for d in range(1, 51, 2) :      # range(start, end, step)
    print(d)
        
# The above code will print only the odd numbers from 1 to 50

# By default the start number is zero
for x in range(61) : 
    print("Abadabadu!")     # This will print the string 60 times

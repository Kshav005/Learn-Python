# The another important concept is taking input from the user
# We can take input function by using input()
# Generally, the input taken is in string data type.
input()

# We can also add a sentence!
input("Enter a word here : ")

# We can assign a variable for taking input and then-
a = input("What is your name - ")
print(a)    # Returns the user's input

b = input("Enter first number : ")
c = input("Enter second number : ")

print(b+c)  # This will not give the preferred output because as told earlier the input fuction accepts the input as string

# So first you need to change the taken information into integer
b = int(b)  # This will overwrite the variable and give it the integer value of the user input
c = int(c)

print(b+c)  # Now the program will be working as you want to!

# Make sure you don't type any string in the output otherwise the program will fail to change it into an integer
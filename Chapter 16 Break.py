# Break is a keyword in Python which stops the loop when a condition when a certain condition is met

for i in range(0, 10) : 
    print(i)
    if i == 5 : 
        break   # When the variable 'i' will become 5, then it will stop the loop
print("The loop has been stopped")

# Same can be used in while loop!
a = 0   
while a == 0 :      # This loop will run continuoesly
    b = int(input("Enter a number : "))
    if b == 17 : 
        break 
print("You entered 17, hence the loop stopped")
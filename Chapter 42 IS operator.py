# 'is' is a comparing operator in python
# It works same as '==' but is still different as it checks the exact location of the value in memory while '==' checks if the value is same

a = input("Enter a number : ")
if a > 10 : 
    print("Greater than 10")
elif a is 10 : 
    print("Equal to 10")
else : 
    print("Lesser than 10")
    
# But they show different output in mutable data types
l = [1, 3, 4]
t = [1, 3, 4]

print(l is t)       # This will return False
print(l == t)       # This will return True

# That's all! You can use 'is' just like '==' in some cases
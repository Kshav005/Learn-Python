# There is a shorter way to use the conditional if else statements
# They make python codes more understandable 
# The syntax is => 'value_if_true if condition else value_if false'
 
a = 34
b = 35

print("34 is bigger") if a>b else print("35 is bigger")
 

# One more example with elif
c = 110
d = 132

print("110") if c>d else print("equal") if c==d else print("132")


# By using this method, you can reduce the number of codes and manage the programs easily as it's easily readable
# There is one more complex thing which you can see below

e = 32
f = 23

result = "None" if e > f else "equal" if e == f else "What?"
print(result)

# The above code is same as : 
if e > f : 
    result = "None"
elif e == f : 
    result = "equal"
else : 
    result = "What?"
print(result)

# You can see, we wrote such a big code in a single line without repeating the variable again and again!
# Short If Else can be used in easy codes but not suitable for complex codes.
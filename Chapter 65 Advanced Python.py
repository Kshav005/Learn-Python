# Welcome to the later part of Python tutorial, where we are going to study about advanced features and operators which you can use in your script!
# Let's start!

# 1. Walrus Operator
# It is an operator which is used to assign values to variables as a part of an expression.
n1 = [1, 3, 5]
for i in range(0, len(n1)) :            # EARLIER
    print(n1[i])

for i in range(0, len(n2:=[1, 3, 5])) :     # USING WALRUS OPERATOR
    print(n2[i])

# Now you can access the variable without any problem!
print(n2)


# 2. Type Definition
# You can now specify the variable type beforehand in python!
a:int = 4.5
b:str = "They"
print(a)

# You might have seen the same in some functions which go like
def add(a:int, b:int) -> int :
    print(a+b)
add(4,5)                

# '->' operator is used to specify the type of 'return'. Using ':' with parameters specifies the type of values that should be entered. Of course, it won't show any error but it helps the reader to understand what they can expect from the function.


# 3. Type Hints
# Done using the module 'typing'
from typing import List, Tuple, Dict, Union

# C++ users might related
# It specifies the type of value a collection hold

# List of integers
lis : List[int] = [3, 4, 5, 6]

# List of Tuple holding strings and float numbers
tup : Tuple[str, float] = ["Hi", 4.7]

# Union is a variable which holds multiple values
s : Union[str, int] = "J33"

# Dictionary
d : Dict[str, int] = {"H":4, "T":8}


# 4. Match-case
# If you know C language or Javascript, you will be familiar with it. It's actually known as 'switch-case' statements in those languages and it works very similar to 'if-else'
# Using 'match', you need to specify the variable which needs to be focused on and then you use 'case' to specify the conditions
t = 10
match t :
    case 50 :                   
        print("No")
    case 70 :
        print("No")
    case 10 :
        print("Yes")
    case _ :                    # Default (else)
        print("?")


# 5. Merged Dictionary
# You can now merge dictionaries in python!
a1 = {"a":1}
a2 = {"b":2, "c":3}
a3 = {"d":90, "z":10}
print(a1|a2|a3)                 # Use '|' to merge


# 6. File I/O
# Now you can open more that 1 file!
with (open("sample1.txt") as f1, open("sample2.txt", "w") as f2) :
    r = f1.read()
    f2.write(r+" Written by original file!")


# 7. Custom Error Message
a = 7
b = 0
if b == 0 :
    raise ZeroDivisionError("This is incorrect :(")         # The way of writing custom error messages

# 8. Enumerate function
# This is a helpful way to get the index number along with the elements in an iterable (list, tuple, etc)
lis = [2,4,5,6,7]
for i, element in enumerate(lis) :
    print(i+1, element)                 # i represents index number while 'element' is the element of that index

# This chapter is completed! Hope you understood some of the recently added features of python.
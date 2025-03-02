# Regular expressions are short symbols which are used to define a function. There are a lot of symbols in python!
# However use them for hard, long and complicated codes and not for basic codes as for loops and 'in' can be used in basic codes
# Use these expressions by importing 're' module, which is built-in

import re

a = '''Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
including structured (particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library'''

# To check if a given word in the string/para is there or not
pattern = "code"
match = re.search(pattern, a)
print(match)


# There are different types of meta characters used in python 
# []    =>      represent a character class
# ^     =>      matches the beginning
# $     =>      matches the ending
# .     =>      matches any character except newline 
# ?     =>      matches zero or one occurence
# |     =>      matches with any of the characters, seperated by it (means OR)
# *     =>      matches any number of occurences including 0 occurence
# +     =>      matches one or more occurences
# {}    =>      indicates the number of occurences

# [], to check character class (sequences like A to Z, P to V, C to T, etc)
pattern2 = "[a-z]rogramming"
match2 = re.search(pattern2, a)     # search is used to find the first occurence
print(match2)

# To get all the occurences
pattern3 = "is"
match3 = re.finditer(pattern3, a)
for i in match3 : 
    print(i)

# Make sure you try the other regular expressions out by yourself!
# This topic is pretty long one, so don't just dissolve yourself on this chapter and check out in the 're' module documentation




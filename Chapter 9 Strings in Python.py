# We will be learning strings a little closely
# Actually the characters use are formed of UNICODE characters
a = "Hello"
b = 'Where'

# The above both are strings, and they are same
print(a, b)     # We can print the strings like this by using variables

# What if we write this?
print(a[0])     # This will return the first character of the string

# This is to note that in Python, the position of characters start from 0(zero).
print(a[4])

# Make sure the position you mentioned above is not out of range, means, you enter 10 even if the string has only 6 characters.
# Otherwise, it will give an error

# If you want to know the length then use len() function
print(len(a))

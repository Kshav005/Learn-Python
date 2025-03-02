# We are going to observe in string slicing
# As we know, any string has number of length
# for example, "apple" has 5 characters

# If we want to print certain number of characters from string.
a = "There"

# We will use slicing, "string[start : end]", the 'end' will not be included in the output, remember that
print(a[0:3])
print(a[1:2])       # Use only square brackets for slicing or indexing

# If you don't write the 'start' then python assumes it as zero(0).
print(a[:4])

# There is another type of indexing!
# From start to end (left to right), it goes from 0,1,2,3,4....
# Whereas, from end to start (right to left), it goes from -1,-2,-3,-4... and so on

print(a[-1])        # Prints the last character of the string
print(a[-5:-2])     # Prints the string from the range
print(a[2:-1])      # We can also mix two different indexing

# But make sure the format of information is [start : end], doesn't matter whatever the index you consider.

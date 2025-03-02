# Typecasting is the conversion from one data type to another data type
# We can change a data type if a number is in form of string
# Type of typecast functions => dict(), str(), float(), int(), tuple(), list(), hex(), ord(), set(), oct(), etc.
# These functions will help in changing data type
# But you cannot change "character here" to integer but "number here" to integer can be done.
a = "5"
b = 3
c = int(a)      # Using int() will change the string 'a' to integer
print(c+b)      # We assigned the new integer 'a' to new variable 'c'

# Using such functions to change data type is known as explicit typecasting

# But sometimes python changes the data type internally, this is known as implicit typecasting
print(4.5+3)        # Integer + Float = Float


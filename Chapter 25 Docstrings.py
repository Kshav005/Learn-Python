# Docstrings are the information regarding function usage. Mostly used in module created functions
# Here is how to create a docstring
def eri(a, b) : 
    '''This functions helps to add two numbers'''
    c = a + b
    print(f"The sum of {a} and {b} is {c}")

eri(4,5)
# Let's print the docstrings
print(eri.__doc__)

# If you find it a little bit complicated then don't worry. It's not compulsory to learn this as it is only used during module making.
# You will understand it's importance later on
# Always written just below the 'def' part!

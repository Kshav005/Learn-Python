# Generators are a special type of fuctions which help you to create an iterable sequence of values
# It is used to generate a list of random values
# Use 'yield' and 'next()' to get those random results

def gen() : 
    for i in range(10000) : 
        yield i 

a = gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# We could also use a list and return its elements but it will take time to create such a large list
# And it will also consume a lot of memory. Thus, you can use this to generate numbers without wasting any extra memory
# Function caching is a way to reduce the time taken by it to complete a particular task
# Generally a program stores cache in the memory. There is a way to access this cache using the module 'functools'

import functools
import time

@functools.lru_cache(maxsize=None)
def abc(x) : 
    time.sleep(4)
    return x+10

print(abc(5))
print(abc(55))
print(abc(14))
print(abc(13))
print(abc(9))
print(abc(4))
print(abc(5))       # from here, the program will start running faster as the values were already stored in the cache memory, so now it doesn't need to calculate it again
print(abc(55))
print(abc(9))
print(abc(4))

# The term memoisation is used to refer as storing a small amount in memory to prevent conputation of the same value again
# Use this if you have a lot of function call with same value
# Otherwise, it won't be much suggested
# Remember, the cache is stored only when the program is ran
# If you run the program again, then the cache is cleared.
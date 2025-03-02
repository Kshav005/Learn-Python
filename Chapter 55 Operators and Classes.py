# We can also define operator magic methods in a class
# Before we can continue, let's talk about a little regarding vectors
# 4i + 3j + 5k, this is a vector. 
# 64i + 23j + 232k, this is also a vector
# Vectors are written by using i, j and k
# Try to gather up some addition of vectors basics
# (4i + 5j + 7k) + (i + 3j + k) = 5i + 8j + 8k
# Only elements with same alphabet are added together, that's all

class Vector : 
    def __init__(self, i1, j1, k1) :
        self.i1 = i1
        self.j1 = j1
        self.k1 = k1
        
    def __add__(self, x) :
        return Vector(self.i1+x.i1, self.j1+x.j1, self.k1+x.k1)
        
    def __str__(self) :         # It is used to decode the python gibberish regrading object information
        return f"{self.i1}i + {self.j1}j + {self.k1}k"
    
a = Vector(4, 5, 7)
b = Vector(1, 3, 1)
print(a + b)            # Hence we changed the old feature to new vector add feature, hence we overloaded an operator 
    
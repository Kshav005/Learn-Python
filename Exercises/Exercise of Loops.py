# In this exercise, you are required to print a star pattern in the following manners.
# Make sure you store the pattern code in a form of a function as this exercise would be having multiple questions. Let's start!
# 1. Square pattern
#               * * * *
#               * * * *
#               * * * *
#               * * * *

# 2. Increasing triangle pattern
#               *
#               * *
#               * * *
#               * * * *
#               * * * * *

# 3. Decreasing triangle pattern
#               * * * * *
#               * * * *
#               * * *
#               * *
#               *

# 4. Right Side triangle pattern
#                       *
#                     * *
#                   * * *
#                 * * * *
#               * * * * *

# 5. Pyramid pattern
#                  *
#                 * *
#                * * *
#               * * * *
#              * * * * *




def squarePattern(n=4):
    for _ in range(n):
        print("* "*n)
        
def increasingTrianglePattern(n=5):
    for i in range(n):
        print("* "*(i+1))   
        
def decreasingTrianglePattern(n=5):
    for i in range(n, 0, -1):
        print("* "*(i))  
          
def rightTrianglePattern(n=5):
    for i in range(n, 0, -1):
        print("  "*(i-1)+"* "*(n-i+1))   
         
def pyramidPattern(n=5):
    for i in range(n, 0, -1):
        print(" "*(i)+"* "*(n-i+1))   
        
        
squarePattern()
print()
increasingTrianglePattern()
print()
decreasingTrianglePattern()
print()
rightTrianglePattern()
print()
pyramidPattern()

# Hence this exercise is completed! Now you can move to next exercises :D
# So today we are going to study about another cool module known as 'Asyncio' and it will help you to save time.
# This module is a built-in module 

import asyncio
import time

# To run all the functions at once, we use the keyword 'async' and 'await'.
async def fun1() : 
    time.sleep(2)
    print("fun1 has been printed!")
    
async def fun2() : 
    time.sleep(2)
    print("fun2 has been printed!")
    
async def fun3() : 
    time.sleep(2)
    print("fun3 has been printed!")
    
async def main() : 
    await fun1()
    await fun2()
    await fun3()
    
asyncio.run(main())     # It will run the functions in the background, so that python doesn't run in sequence



# Hence the Python Programming has came to an end, now you may learn modules to go into the fields like Data Science, Machine Learning, Web Development and many more!
# Thank you for reading out all this and congrats, you have learnt Python! You may practice and create different projects now
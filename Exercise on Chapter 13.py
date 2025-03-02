# So, for this exercise, create a program to greet a user according to the time of the day!
# Use conditions from Chapter 12 to wish either Good morning, good afternoon or good night.
# If tried but failed, look at the solution below.
# Also, you did a great job as you have come this far!








import time 
ask = input("What is your name : ")
t = time.strftime("%H")

if t < "12" : 
    if t > "05" : 
        print("Good Morning!", ask)  
    else : 
        print("You are still awake :0", ask)
elif t > "12" : 
    if t > "18" : 
        print("Good Night", ask)
    else : 
        print("Good afternoon :D", ask)
# In this exercise, create a small question answer bot with the help conditions and string attributes!
# You can also use while loop and lists for some cases if you like but if you can create a question answer bot without it, then it's not a big deal!
# Solution is given below, but make sure you try it yourself first. Good Luck!!





a = input("Do you want to play QNA game? Type Y or N")
if a == "Y" : 
    print("Let's get started!")
    b = input("Q1 - Which animal has the longest neck?")
    if b.lower() == "giraffe" : 
        print("That's the correct answer! Next question")
    else : 
        print("Oh no :(, wrong answer.  Next question anyway.")
        
    c = input("Q2 - Which continent is the largest in the world?")
    if c.lower() == "asia" : 
        print("Another correct answer my friend!")
    else : 
        print("Wrong answer! Beep!")
        
# The exercise has been completed, you can add more questions if you want! 
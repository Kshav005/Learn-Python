# This is another concept! Make sure you know this.
# This comes under decision making. It is the first and the most basic condition to create Artificial Intelligence.
# Colon(:) is must in If Else.
a = input("Where are you from?")

if a == "india" :       # if can be written alone also without 'else' 
                        # make sure you use double equal symbol(==) as single equal is to mark value for a variable
    print("Hello fellow indian!")   # Adding space to show that this comes under the 'If' condition (Known as indentation)
    print("This is indentation!")

elif a == "USA" :       # 'elif' is to add another condition. Infinity number of 'elif's can be used!
    print("American! I can speak english!")
    
else :      # else doesn't need any condition to meet, it will perform the action as soon as the condition is not met from the 'if'
            # else cannot be used alone
    print("Oh cool, foreigner!")
    
# As python is case sensitive('A' and 'a' are different for python), so if we write IndIa or India or anything, then it would print the statemoent of else
# Conditional operators are used in If Else like, >, <, ==. !=, >=, <= etc.
# This chapter will be easy for those who know flowcharts! They will be able to tell how is the flow of the code.

print("I am not in the if else statements :p")  # This will not come under any condition as indentation is absent, so it will run no matter what the condition is

# You can also use if statement under another if statement too!
yu9 = 23

if yu9 > 20 : 
    if yu9 < 25 : 
        print("Meow")
    else : 
        print("What?")
else : 
    print("No Meow")
    
# This type of above if statement is known as 'nested if'.
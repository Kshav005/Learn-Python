# In this exercise, your job is to create a encode program. 
# The program should be taking input from the user and if the length of the input is less or equal to 3, then the program should remove the first letter, append that first letter to the end of the word and then add three random alphabets in both start and in end.
# Otherwise, the input word should be reversed and printed out
# This program is really complicated, so make sure you have learnt all the concepts and attributes of lists and strings
# More attributes can be found in documentation of python. Just search 'python documentation' on your web browser.
# Also, you will be needing a new module called 'random' to complete the program.
# So nake sure you import and read its documentation 
# That's all! Now good luck and don't worry if you fail to create one.
# The solution is given below. Try to understand it







import random 

empstr = ""         # Creating empty string
emplis = []         # Creating empty list
 
a = input("Enter a word : ")        # Asking for the word
b = a.split()                       # Changing the string in form of string
if len(a) <= 3 :                    
    alphabet = "abcdefghijklmnopqrstuvwxyz"     # Creating a variable 
    randomalphalist = []                        # Then creating an empty list to append all the characters in this list
    for x in alphabet : 
        randomalphalist.append(x)               # Appending all those characters
    c = b[0][0]                                 # Accessing the first element's first character
    for i in a : 
        emplis.append(i)                        # Changing the input string into list
    emplis.pop(0)                  # Deleting the first character of the list
    emplis.append(c)               # Using append to put that first letter in the end of the list
    for y in range(1, 4) : 
        randomendalpha = random.choice(randomalphalist)     # Using the module to get random alphabet
        emplis.append(randomendalpha)                       # Appending to insert 3 random alphabets in the end of the list
    for y1 in range(1, 4) :                                 # Using loop 3 times to get 3 random alphabets 
        randomstartalpha = random.choice(randomalphalist)   
        emplis.insert(0, randomstartalpha)                  # Then, inserting those three alphabets in the start
    re = empstr.join(emplis)                                # Converting the list to string by joining those elements together
    print(re)                                               # Printing the result
else : 
    for i in a :                                            # If the length is more than 3, then reversing the order
        emplis.append(i)
    emplis.reverse()                                        # To reverse the order of elements in a list
    re = empstr.join(emplis)
    print(re)
        

# I know it's really hard and confusing exercise but it will help you to understand attributes better
# The exercise is over! Congrats
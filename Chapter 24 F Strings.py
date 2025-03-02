# f-strings help to place a variable in a string easily!
# f-strings = format-strings
a = input("Enter your name : ")

# Earlier you needed to add a comma to use the variable value
print("Hello,", a, "! How are you?")

# But now you can use an easier and efficient way without having much difficulty in adding quotes again and again
# Make sure you add an 'f' before the starting quote and use the variable value surrounded with curly brackets.
print(f"Hi {a}! Hope you are doing great!")

# There is another way to use format.
# The above one was a short and easy, this below one is a little lengthy but helpful
# In this one, you needn't add an 'f' but instead you need to use 'format(variable_name)'
print("Hey {}, how are you my friend?".format(a))

# Remember to use the variables in the order if there are more than two variable values to be added in string

# You can also perform calculations!
print(f"The value is {3*5}")
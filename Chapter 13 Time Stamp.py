# Modules are like books
# Suppose you want to know about something, you will pick up any book from other books even if they all are written for the same topic.
# Just like that modules are files, which makes our work easier!
# There are many modules but we will only pick up one.
# Just like all those books in above example are written in english, here all the modules, even if some do same tasks, are written in python language!
# Modules are imported through 'pip install module_name' in the shell.
# Shell is the window where you output statement is written
# Our module name is time, so we import these modules by using 'import module_name'
# Time is a built-in module in python. It has many methods which can be used to solve various problems.
import time

# To get the current time in format
timest = time.strftime("%H:%M:%S")      # %H = hours, %M = minutes, %S = seconds
print(timest)

# Before continuing 'epoch' is a time where the time module starts, January 1, 1970, 00:00:00
# Suppose we want to get, how long a function has been ran
a = time.time()                         # gives the number of seconds gone since epoch
for i in range(5000) : 
    print(i)
b = time.time() - a                     # Taking out the difference
print(f"The program took {b} seconds to end!")

# To take a small break or wait before running another line of code, 'time.sleep(seconds)'
time.sleep(1)
print("Nice")

# Accessing files in a computer is as important as writing codes
# We learn OS module but that is just used to manipulate files and folders and not edit or read a certain file
# To get that feature, python has various syntaxes to do so!

# There are mainly 3 types of modes to access a file - 'r'(read), 'w'(write), 'a'(append)
# There are other modes too, such as -
# r => You can only read the whole file or some lines. Cannot edit and gives error if file doesn't exist
# w => You can write the whole file but it will clear and rewrite the old content of the file. Creates a new file if file doesn't exist
# a => It does the same work as 'w' but the difference is that the cursor is at the end of the file, which means, the old content will still be there and the file will get written with the old content existing.
# x => It only creates a file, gives error if file exists
# b => used to handle binary files, used with 'r' and 'w'

# We can also read and write files in binary! But that would be covered in further chapters
# To access file => 'open("file_name.txt", "mode_name")
f = open("nothing.txt", "w")

# To write content in the text file
f.write("Hello my friend!\nThere is a cat\nNothing is for free :(")     
f.close()       # Remember to close the file, once the work is done

# If you run the above code, then you will see that a new text file will be created with the content written!


# To append the file 
a = open("nothing.txt", "a")
a.write("What are you talking about?")
a.close()


# To read the file
g = open("where.txt", "r")

h = g.read()                # Will read the whole file and returns in form of a string
i = g.readline()            # Will read only the number of line provided in the brackets
j = g.readlines()           # Will return in form of list, works same as readline
print(h)
print(i)
print(j)
g.close()


# To write lines from a list 
lis = ["meow\n", "what\n", "no\n", "yes\n"]
z = open("nothing2.txt", "w")
z.writelines(lis)
z.close()
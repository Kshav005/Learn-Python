# So we are going to see some most popular functions used while accessing files!
# Both these functions are important for accessing characters from various indexes

# There is another way to open a file, which automatically closes itself and we needn't write '.close()' everytime
# Syntax => 'with open("file_name.txt", "mode_name") as variable_name'

# The seek() function allows you to move the cursor after some characters provided by you.
with open("nothing.txt", "r") as f : 
    f.seek(2)               # To move to the place
    a = f.read(10)          # To read the first 10 characters after that place
    print(a)
    
    # The tell() function tells the index till you have seeked. Below will print '12' as you started after 2 then read 10 characters after it. It means you have seeked total 10+2 = 12 characters in the file
    print(f.tell())

# To restrict the file from writing characters after certain index, we use truncate() function
with open("nothing3.txt", "w") as t : 
    t.write("There was a boy who helps everybody.")
    t.truncate(10)      # We want python to write only first 10 characters 


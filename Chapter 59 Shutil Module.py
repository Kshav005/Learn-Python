# A 'Shutil' module is like 'os' module and it is used to work through files and folders
# It is also a built-in module
import shutil

# To copy a file into another file 
shutil.copy("Chapter 59 Shutil Module.py", "Open this during Chapter 59.py")

# To copy a file into another file, including metadata (file created date, time, etc)
shutil.copy("Chapter 59 Shutil Module", "WOW.py")

# To copy a while folder (shutil.copytree("file_name", "new_name_for_copy"))
shutil.copytree("Nothing", "NothingCopy")

# To move the file into another directory 
shutil.move("create.pdf", "User/create.pdf")

# To delete a folder (there is no command to delete a file. Use OS module for that)
shutil.rmtree("FOlderHere")





# OS module is another main module which is of great help in future.
# It is the most useful in creating web apps or games
# It can delete every file from your computer or copy a file or anything
# It is a built-in python library so you need not install it externally.

import os 

# To create a folder 'os.mkdir("folder_name")
os.mkdir("emp")

# To make various numbers of folders, this is very cool function as it is very hard to create more than 20 folders manually
for i in range(1, 101) : 
    os.mkdir(f"emp/Folder{i}")

# To rename folders, this is another cool feature because it will take ages to rename 30+ folders
for i in range(1, 101) : 
    os.rename(f"emp/Folder{i}", f"emp/RenameFolder{i}")     # 'os.rename("original_file_name", "new_file_name")
    
# To get list of folders in a folder (will return a list having folder names as elements)
numfold = os.listdir('emp')
print(numfold)  
print(len(numfold))                 # To check how many folders are there

# To get the folder name (directory) in which you are currently in
print(os.getcwd())

# To delete a file
os.remove("Nothing.txt")

# To delete an empty folder 
os.rmdir("users/Nothing")

# Make sure you read its documentation online! 
# There is a lot of information to gain through this module.
  
# Let's continue with the advanced version of python and let's start with Virtual environment.
# It is created in order to isolate the system interpreter from other environments. Basically, think it as a mini computer which uses it's own installed modules, etc and can use older versions of a particular module too!
# Older versions can also be installed without virtual environment but it will replace your newer version of that module.
# So, think this of an another PC where you can keep different versions. But it's actually inside a single PC!
# To use it, first install virtualenv using 'pip install virtualenv' in the terminal.
# Then type 'virtualenv x' in the terminal, where 'x' can be any name required for the virtual environment. I named it as 'e1'.
# If you are using VS Code, an menu will appear at the bottom right side. Click 'Yes'. Now you will be inside your environment and a folder will be created.
# To activate your environment, type '.\x\Scripts\activate.ps1' in the cmd.
# Make sure, the terminal is directed to the file location where the environment folder is stored.  
# In the beginning of every terminal line, you will see your environment name in brackets, which means activation was successful!
# Now try 'pip install howdoi'
# This will install the module only in this environment. When you switch the interpreter, you will not be able to use this module. If doubted, type 'howdoi pull a repository' in the terminal of both the environments (virtual and default/original environment)

# Now, if you like to know about all the packages installed in your PC, then you can type 'pip freeze' in the terminal.
# This command will show the list of installed modules according to environment you are working in. By default, PC works in the default environment.
# To store all these things in the text file, we can type 'pip freeze > filename.txt'

# Suppose you save this folder in a git repository. How will you tell the user to install the modules that you have used? Of course, you can send the name to the receiver, but do you think he can install 20 modules if you used that many in your work? No.
# Therefore, you can type 'pip install -r .\filename.txt' to install every module written in the file one by one. Making it easier for you to share requirements!
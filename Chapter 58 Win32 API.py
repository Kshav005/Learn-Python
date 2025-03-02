# In this chapter, we are going to learn about a new module called 'win32'
# We are going to use the text to speech here!
# It is a built-in module of python

import win32com.client

speak = win32com.client.Dispatch("SAPI.SpVoice")

a = input("Enter the word that you want the computer to speak!\n")
speak.Speak(a)


# In this exercise, you need to use the text to speech feature and create another QNA bot, where the bot asks the question by speaking
# Good luck, and if you couldn't solve then you can look at the solution below.







import time 
import random
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
correctlist = ["Wow, you did a great job!", "Correct answer!", "Good Job", "Nice, you did great!", "Woah, you are really smart.", "Beep Boop. Correct Answer!"]
incorrectlist = ["No, that's not correct", "Oops, wrong answer", "You gave an incorrect answer", "Guess, you were not that smart", "Incorrect!", "Poor choice. That is incorrect"]
incorrect = random.choice(incorrectlist)
point = 0

a1 = "Welcome to the question answer bot!"
print(a1)
speaker.speak(a1)
time.sleep(0.5)
a2 = "Let's go with the first question"
print(a2)
speaker.speak(a2)
time.sleep(0.5)
a3 = "What is the first alphabet?"
print(a3)
speaker.speak(a3)
time.sleep(0.5)
a4 = "Option 1. A"
print(a4)
speaker.speak(a4)
a5 = "Option 2. Z"
print(a5)
speaker.speak(a5)
a6 = "Or option 3. P"
print(a6)
speaker.speak(a6)
a7 = "Type the option NUMBER"
print(a7)
speaker.speak(a7)

q1 = int(input())
if q1 == 1 : 
    correct = random.choice(correctlist)
    print(correct)
    speaker.speak(correct)
    point = point + 1
else : 
    incorrect = random.choice(incorrectlist)
    print(incorrect)
    speaker.speak(incorrect)


a33 = "What is the capital of USA?"
print(a33)
speaker.speak(a33)
time.sleep(0.5)
a44 = "Option 1. Delhi"
print(a44)
speaker.speak(a44)
a55 = "Option 2. Singapore"
print(a55)
speaker.speak(a55)
a66 = "Or option 3. Washington D.C."
print(a66)
speaker.speak(a66)
a77 = "Type the option NUMBER"
print(a77)
speaker.speak(a77)

q1 = int(input())
if q1 == 3 : 
    correct = random.choice(correctlist)
    print(correct)
    speaker.speak(correct)
    point = point + 1
else : 
    incorrect = random.choice(incorrectlist)
    print(incorrect)
    speaker.speak(incorrect)


a333 = "What computer language are we learning?"
print(a333)
speaker.speak(a333)
time.sleep(0.5)
a444 = "Option 1. Java"
print(a444)
speaker.speak(a444)
a555 = "Option 2. C++"
print(a555)
speaker.speak(a555)
a666 = "Or option 3. Python"
print(a666)
speaker.speak(a666)
a777 = "Type the option NUMBER"
print(a777)
speaker.speak(a777)

q1 = int(input())
if q1 == 3 : 
    correct = random.choice(correctlist)
    print(correct)
    speaker.speak(correct)
    point = point + 1
else : 
    incorrect = random.choice(incorrectlist)
    print(incorrect)
    speaker.speak(incorrect)

a123 = "The game is over now!"
print(a123)
speaker.speak(a123)
a1234 = f"Your total score is {point}"
print(a1234)
speaker.speak(a1234)


b11 = "Therefore, the exercise is complete! You may add more questions just like these."
speaker.speak(b11)


# In this exercise, you need to create a drink water reminder, in which the python sends a notification every 'n' number of seconds/hours/minutes to the user to drink water.
# Import the plyer module to use the notification system in your PC. 
# Then use you knowledge from previous chapters to create this thing
# Good luck, I know you will do it!
# If you failed, don't worry. You have came far, congrats to you for that.
# Below is the solution, try to understand it more and create meaningul programs like this in the future!

















from plyer import notification 
import time 

a = input("Do you want to get reminded to drink water? Yes or No?\n")
if a.lower() == "yes" :
    print("Alright! Enter the number if you want to get reminded every\n1.n Hour\n2.n Minute\n3. n Second")
    b = int(input())
    if b == 1 : 
        how = int(input("After every how many hours? Enter the number : "))
        seconds = how * 3600
        while True : 
            time.sleep(seconds)
            while True : 
                notification.notify(title = "DRINK WATER", message = "Time to drink water!", timeout = 5)
                ask = input("Drank Water?\nYes or No : ")
                if ask.lower() == "yes" : 
                    time.sleep(1)
                    ask2 = input("Do you want to continue? : ")
                    if ask2.lower() == "yes" : 
                        print(f"Nice! I will come back after {how} hour(s) again 😾")
                        break
                    else : 
                        time.sleep(1)
                        print("Okay! Exiting in few seconds...")
                        time.sleep(2)
                        exit()
                else : 
                    continue

    elif b == 2 : 
        how = int(input("After every how many minutes? Enter the number : "))
        seconds = how * 60
        while True : 
            time.sleep(seconds)
            while True : 
                notification.notify(title = "DRINK WATER", message = "Time to drink water!", timeout = 5)
                ask = input("Drank Water?\nYes or No : ")
                if ask.lower() == "yes" : 
                    time.sleep(1)
                    ask2 = input("Do you want to continue? : ")
                    if ask2.lower() == "yes" : 
                        print(f"Nice! I will come back after {how} minute(s) again 😾")
                        break
                    else : 
                        time.sleep(1)
                        print("Okay! Exiting in few seconds...")
                        time.sleep(2)
                        exit()
                else : 
                    continue
    elif b == 3 : 
        how = int(input("After every how many seconds? Enter the number : "))
        while True : 
            time.sleep(how)
            while True : 
                notification.notify(title = "DRINK WATER", message = "Time to drink water!", timeout = 5)
                ask = input("Drank Water?\nYes or No : ")
                if ask.lower() == "yes" : 
                    time.sleep(1)
                    ask2 = input("Do you want to continue? : ")
                    if ask2.lower() == "yes" : 
                        print(f"Nice! I will come back after {how} second(s) again 😾")
                        break
                    else : 
                        time.sleep(1)
                        print("Okay! Exiting in few seconds...")
                        time.sleep(2)
                        exit()
                else : 
                    continue
    else : 
        print("Wrong Input, Exiting......")
        time.sleep(3)
        exit()
        

# Hence the exercise is complete!
        

# Here are the list of questions that you need to perform!
# Good luck. Also, the solution is provided below the questions, though, try to do it yourself first!

# Q1 - Write a program to open three files 1.txt, 2.txt & 3.txt, if any of these files are not present, a message should be popped up without exiting the program 

# SOLUTION
try :
    with (open("1.txt"), open("2.txt"), open("3.txt")) :
        print("All files are present")
except Exception as e:
    print("Error occured :", e)




# Q2 - WAP to print third, fifth and seventh element from a list using enumerate and match-case.

# SOLUTION
lis = [3, 4, 6, 2, 3, 5, 10, 7, 9]
for i, e in enumerate(lis) :
    match i+1 :
        case 3 :
            print(f"Element {i+1} : {e}")
        case 5 :
            print(f"Element {i+1} : {e}")
        case 7 :
            print(f"Element {i+1} : {e}")





# Q3 - WAP using list comprehension to print a list having multiplication table of the number entered by the user.

# SOLUTION
n = int(input("Enter a number : "))
l = [n*x for x in range(1, 11)]
print(l)


# This exercise has been completed, congrats!
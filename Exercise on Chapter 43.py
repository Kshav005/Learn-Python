# In this exercise, you have to create a Library like Management system, where you can add books, get the list of all books and get the number of books present.
# Don't forget to use the OOP here!
# If you are unable to solve then below is the solution but make sure you give this exercise a try yourself.
# Trying is more than enough! Also use the time module for pauses in between if possible, otherwise it's fine too.










import time


class Library : 
    def __init__(self) :
        self.li = []
        
    def add_book(self, name) : 
        self.li.append(name)
        
    def total_books(self) : 
        t = len(self.li)
        print(f"Total number of books are {t}")
    
    def all_books(self) : 
        for i in self.li : 
            print(i)

book = Library()
while True : 
    time.sleep(0.5)
    print("____________________________________Library Management System____________________________________")
    time.sleep(1)
    print("1. ADD A BOOK\n2. TOTAL NUMBER OF BOOKS\n3. LIST OF ALL BOOKS\n4. EXIT")
    a = int(input("Enter your choice in terms of numbers : "))
    time.sleep(1)
    if a == 1 : 
        b = input("Enter the name of the book : ")
        book.add_book(b)
        time.sleep(0.5)
        print("Book added successfully!")
    elif a == 2 : 
        book.total_books()
    elif a == 3 : 
        book.all_books()
    elif a == 4 : 
        print("Exiting the Program.......")
        break
    else : 
        print("Wrong Input")
        break
        

# Hence the exercise is complete! Congrats friend!!
        
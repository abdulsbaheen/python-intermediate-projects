import time 


class Library:

    def __init__(self):
        self.books = []
        self.no_of_books = len(self.books)

# dipllay funtion to display the total no of books and the name of the books in the library

    def display_info(self):
        print(f"\nThere are {self.no_of_books} total no of books.")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}.{book}")
# add function to Add book

    def add_book(self, add):
        self.books.append(add)
        print(f"\nThe {add} book 📔 has added to your library.")
# borrow function to borrow book and remove it from the library

    def borrow_book(self, borrow):
        if borrow in self.books:
            self.books.remove(borrow)
            print(f"\nYou have borrowed {borrow} book.")
            print("Please return it in 30 days. Thank you!🙌")
        else:
            print(f"\n Sorry, {borrow} book is not available in the library.")

# return function to return book and add it to the library
    def return_book(self, Return):
        self.books.append(Return)
        print(f"\nYou have returned {Return} book. Thank you!🙌")

# child libraries for different subjects

# computer science library
class comp_Library(Library):
    def __init__(self):
        super().__init__()
        self.books = ["Python Programming",
                      "Data Science",
                      "Machine Learning",
                      "Artificial Intelligence",
                      "Deep Learning"]
        self.no_of_books = len(self.books)

# chemistry library
class chem_Library(Library):
    def __init__(self):
        super().__init__()
        self.books = ["Organic Chemistry",
                      "Inorganic Chemistry",
                      "Physical Chemistry",
                      "Analytical Chemistry",
                      "Biochemistry"]
        self.no_of_books = len(self.books)

# physics library
class phy_library(Library):
    def __init__(self):
        super().__init__()
        self.books = ["Classical Mechanics",
                      "Electromagnetism",
                      "Quantum Mechanics",
                      "Thermodynamics",
                      "Optics"]
        self.no_of_books = len(self.books)


comp = comp_Library()
phy = phy_library()
chem = chem_Library()

# main program to interact with the user and perform library management system
while True:
    time.sleep(2)
    print("-"*20)
    print("Welcome to library management system")
    print("-"*20)
    time.sleep(1)
    print("\n which library you want to explore or exit the program")
    print("1.computer science")
    print("2.chemistry")
    print("3.physics")
    print("4.exit")
    print("-"*20)
    
    # taking input from user to choose the library they want to explore
    choice_input = input("\nPlease enter the choice b/w 1-4 :")
    time.sleep(1)
    # checking the user input and performing the corresponding library management system
    if choice_input in ('1', '2', '3', '4'):
        
        # if user choose 1 then computer science library management system will be executed
        if choice_input == '1':
            while True:
                time.sleep(1)
                print("-"*20)
                print("Welcome to computer library")
                print("\nwhat function you want to use?")
                print("1. Display all books")
                print("2. Add a book")
                print("3. Borrow a book")
                print("4. Return a book")
                print("5. Exit")
                print("-"*20)
                time.sleep(1)
                user_choice = input("please enter the number b/w (1-5) to perform a task.")
                
                 # checking the user input and performing the corresponding function of the library management system
                if user_choice in ('1','2','3','4','5'):
                    time.sleep(1)
                    if user_choice == '1':
                     print("-"*20)
                     comp.display_info()
                     print("-"*20)
                    elif user_choice == '2':
                      add = input("\nEnter the name of the book you want to add: ")
                      comp.add_book(add)
                    elif user_choice == '3':
                      borrow = input("\nEnter the name of the book you want to borrow: ")
                      comp.borrow_book(borrow)
                    elif user_choice == '4':
                      Return = input("\nEnter the name of the book you want to return:")
                      comp.return_book(Return)
                    elif user_choice == '5':
                      break
                    time.sleep(1)
                else:
                 print("Invalid input. Please enter a number between 1 and 5.")    
        
        # if user choose 2 then chemistry library management system will be executed
        elif choice_input == '2':
                while True:
                    time.sleep(1)
                    print("-"*20)
                    print("Welcome to chemistry library")
                    print("\nwhat function you want to use?")
                    print("1. Display all books")
                    print("2. Add a book")
                    print("3. Borrow a book")
                    print("4. Return a book")
                    print("5. Exit")
                    print("-"*20)

                    user_choice = input("please enter the number b/w (1-5) to perform a task.")
                    
                    # checking the user input and performing the corresponding function of the library management system
                    if user_choice in ('1','2','3','4','5'):
                    
                        if user_choice == '1':
                         print("-"*20)
                         chem.display_info()
                         print("-"*20)
                        elif user_choice == '2':
                          add = input("\nEnter the name of the book you want to add: ")
                          chem.add_book(add)
                        elif user_choice == '3':
                          borrow = input("\nEnter the name of the book you want to borrow: ")
                          chem.borrow_book(borrow)
                        elif user_choice == '4':
                          Return = input("\nEnter the name of the book you want to return:")
                          chem.return_book(Return)
                        elif user_choice == '5':
                          break
                        time.sleep(1)
                    else:
                     print("Invalid input. Please enter a number between 1 and 5.")
        # if user choose 3 then physics library management system will be executed             
        elif choice_input == '3':
            while True:
                time.sleep(1)
                print("-"*20)
                print("Welcome to physics library")
                print("\nwhat function you want to use?")
                print("1. Display all books")
                print("2. Add a book")
                print("3. Borrow a book")
                print("4. Return a book")
                print("5. Exit")
                print("-"*20)
                
                user_choice = input("please enter the number b/w (1-5) to perform a task.")
                time.sleep(1)

                # checking the user input and performing the corresponding function of the library management system
                if user_choice in ('1','2','3','4','5'):
                
                    if user_choice == '1':
                     print("-"*20) 
                     phy.display_info()
                     print("-"*20)
                    elif user_choice == '2':
                      add = input("\nEnter the name of the book you want to add: ")
                      phy.add_book(add)
                    elif user_choice == '3':
                      borrow = input("\nEnter the name of the book you want to borrow: ")
                      phy.borrow_book(borrow)
                    elif user_choice == '4':
                      Return = input("\nEnter the name of the book you want to return:")
                      phy.return_book(Return)
                    elif user_choice == '5':
                      break
                    time.sleep(1)  
                else:
                    print("-"*20)
                    print("Invalid input. Please enter a number between 1 and 5.")
                    print("-"*20) 
        else:
            break
    # if user choose 4 then the program will be exited              
    else:
        print("_"*20)
        print("Invalid input! please enter the valid input")
        print("-"*20)

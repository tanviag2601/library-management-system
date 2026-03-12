from LIB_MANAGE import lib_man
import ADD
import RETURN
import ISSUE
books=["The Alchemist ", "To Kill a Mockingbird"," The Great Gatsby","Animal Farm","Pride and Prejudice"]
obj=lib_man(books)
while True:
    print("Library Menu:")
    print("Enter 1 to view all the books")
    print("Enter 2 to add a new book")
    print("Enter 3 to return a book")
    print("Enter 4 to issue a book")
    print("Enter 5 to exit the program")
    choice=int(input("Enter your choice as stated above "))
    if(choice==1):
        print("Available books: ",books)
    elif(choice==2):
        ADD.add_book(obj,input("Enter name of the new book "))
    elif(choice==3):    
        RETURN.return_book(obj,input("Enter the name of the book which u want to return "))
    elif(choice==4):    
        ISSUE.issue_book(obj,input("Enter the name of the book which u want to issue "))
    elif(choice==5):
        print("Thank you,Exiting the program")
        break
    else:
        print("Invalid input.")  




def return_book(obj2,name_return):#to return a book and compute its fine
         obj2.name_return=name_return 
         obj2.books.append(name_return)    # to add book back which is returned
         print("BOOK RETURNED")
         print("Available books",obj2.books)

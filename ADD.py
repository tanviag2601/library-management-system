def add_book(obj1,name_add): #to add new book
            obj1.name_add=name_add
            obj1.books.append(obj1.name_add)
            print("NEW BOOK ADDED",obj1.books)
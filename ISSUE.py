def issue_book(obj3,name_issue):# to issue a book
         issue=[]
         j=0
         obj3.name_issue=name_issue
         for i in obj3.books:
              if(i==obj3.name_issue):   # if book is present in the library
                   print("Book issued")
                   issue.append(obj3.name_issue)    # to add
                   obj3.books.remove(name_issue)   # to remove from existing
                   return
              elif(i!=obj3.name_issue):     # if book is not present in  the library   
                 j=j+1
         if(j!=0):
            print("Book is not in the library")  
         
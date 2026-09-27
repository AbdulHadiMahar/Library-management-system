import os
class library:
    books = []
    br_books=[]
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def showdetails(self):
            print(f'The book {self.name} is writte by {self.author}')
    @classmethod
    def load_library(cls):
        if os.path.exists('library.txt'):
            with open('library.txt', 'r') as f:
                for line in f:
                    line = line.strip()
                    if 'Book name :' in line and ', Author is' in line:
                         content = line.replace('Book name :', '').strip()
                         parts = content.split(', Author is')
                         if len(parts) == 2:
                             book_name = parts[0].strip() 
                             author = parts[1].strip()
                             cls.books.append(library(book_name,author)) 
    @classmethod
    def load_brBooks(cls):
        if os.path.exists('borrowed_books.txt'):
            with open('borrowed_books.txt', 'r') as z:
              for line in z:
                  line = line.strip()
                  if 'Book name :' in line and ', Author is' in line:
                      content2 = line.replace("Book name :", '').strip()
                      parts2 = content2.split(', Author is')
                      if len(parts2) == 2:
                         brBook_name = parts2[0].strip()
                         brAuthor_name = parts2[1].strip()
                         cls.br_books.append(library(brBook_name,brAuthor_name))                    
library.load_library()
library.load_brBooks()
def menu():
     try:
        return int(input("\nPress 1 to view all books available in library\n"
            "Press 2 to add a book in library \n" 
            "Press 3 to view particular details of book by its name \n" 
            'Press 5 to remove a book from library\n' \
            'Press 6 to borrow a book\n' \
            'Press 8 to return a borrowed book\n'
            "Press 0 to exit : "))
     except ValueError:
        print("Entre a valid integer")
       
while True:
     a = menu()
     match a:
          case 1:
               if len(library.books) == 0:
                 print("There are 0 books in library ")
               else:
                   print(f"There are {len(library.books)} Books in library")
                   for i in library.books:
                       print(i.name)
          case 2:
             name = input("Entre the book name you want to add in library : ")
             authr = input("Entre the Author name of this book : ")
             for i in library.books:
                if name.lower() == i.name.lower():
                 print(f'{name} is already existed in library so not added yet')
                 break
             else:
                 book1 = library(name,authr) 
                 library.books.append(book1)
                 print("The book is added in library succesfully 🎉")
          case 3:
             s1 = input("Entre the name of book you want details of :")   
             for i in library.books:
                     if s1.lower() == i.name.lower():
                      i.showdetails()
                      break   
             else:
                 print(f"The {s1} is not available in library")
          case 5:
             rm =input("Entre the name of book you want to remove : ")
             for i in library.books:
                 if rm.lower() == i.name.lower():
                     library.books.remove(i)
                     print(f'{rm} is succesfullt removed from library')
                     break
             else:
                     print(f'{rm} is not available in library')
          case 6:
             br = input("Entre the book name you want to borrow from library : ")
             for i in library.books:
                 if br.lower() == i.name.lower():
                     print(f' The books {br} is borrowed by you return as soon as possible')
                     library.books.remove(i)
                     library.br_books.append(i)
                     break
             else:
                 print(f'{br} is not available in library')
          case 8:
             ret = input('Entre the book you borrowed and returing now : ')
             for i in library.br_books:
                   if ret.lower()==i.name.lower():
                        print(f'Thanks for returning the book {ret}')
                        library.br_books.remove(i)
                        library.books.append(i)  
                        break 
             else:
                 print(f'{ret} is not borrowed. Entre the right spellings')        
          case 0:
             print('Saving Library to : ', os.path.abspath('library.txt'))
             with open('library.txt', 'w') as f:
                 for i in library.books:
                     f.write(f"Book name : {i.name}, Author is {i.author}\n")
             with open('borrowed_books.txt','w') as z:
                 for i in library.br_books:
                     z.write(f'Book name : {i.name}, Author is {i.author}\n')        
             print('You are out')
             break
          case _:
             print("Entre a valid integer as choice")

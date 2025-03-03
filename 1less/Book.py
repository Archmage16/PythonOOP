class Book():
    def __init__(self, title, year, author, manufactor, book_type, price):
        self.title = title
        self.year = year
        self.author = author
        self.manufactor = manufactor
        self.book_type = book_type
        self.price = price
    
    
    def set_title(self, title):
        self.title = title
    def set_year(self, year):
        self.year = year
    def set_author(self, author):
        self.author = author
    def set_manufactor(self, manufactor):
        self.manufactor = manufactor
    def set_book_type(self, book_type):
        self.book_type = book_type
    def set_price(self, price):
        if type(price) != int:
            return "Error price"
        else:
            self.price = price
            return True

    def get_title(self):
        return self.title
    def get_year(self):
        return self.year
    def get_author(self):
        return self.author
    def get_manufactor(self):
        return self.manufactor
    def get_book_type(self):
        return self.book_type
    def get_price(self):
        return self.price
    
    
    # def Inputs(self):
    #     t = input("Write a book title: ")
    #     self.set_title(t)
    #     t = input("Write a book year: ")
    #     self.set_year(t)
    #     t = input("Write a book author: ")
    #     self.set_author(t)
    #     t = input("Write a book manufactor: ")
    #     self.set_manufactor(t)
    #     t = input("Write a book type: ")
    #     self.set_book_type(t)
    #     while True:
    #         try:
    #             t = int(input("Write a book price: "))
    #             if self.set_price(t):
    #                 break
    #         except ValueError as va:
    #             print(f"Error: {va}")
    #         print("Try again. It isn't city")

    
    def Print(self):
        print(f"Book title: {self.get_title()}")
        print(f"Book year: {self.get_year()}")
        print(f"Book author: {self.get_author()}")
        print(f"Book manufactor: {self.get_manufactor()}")
        print(f"Book type: {self.get_book_type()}")
        print(f"Book price in tenge: {self.get_price()}")


book1 = Book("Harry Potter", "2000", "J.K. Rowling", "Bloomsbury", "Fantasy", 5000)
book2 = Book("The Lord of the Rings", "1954", "J.R.R. Tolkien", "Bloomsbury", "Fantasy", 10000)
book3 = Book("The Alchemist", "1988", "Paulo Coelho", "Allen & Unwin", "Fantasy", 4000)
book4 = Book("fwedq", "1990", "Paulo Coelho", "HarperTorch", "Fantasy", 2000)
book5 = Book("gbrtdgf", "2020", "Me", "HarperTorch", "Fantasy", 10000)


class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def print_name(self):
        book_lists = []
        for i in self.books:
            
            book_lists.append(i.get_title())
        print(book_lists)
    
    def search_author_books(self,author):
        book_lists = []
        for i in self.books:
            if i.get_author() == author:
                book_lists.append(i.get_title())
        print(book_lists)
        
    def search_manufactor_books(self,manufactor):
        book_lists = []
        for i in self.books:
            if i.get_manufactor() == manufactor:
                book_lists.append(i.get_title())
        print(book_lists)
        
    def year_book(self,year):
        book_lists = []
        for i in self.books:
            if i.get_year() >= year:
                book_lists.append(i.get_title())
        print(book_lists)
    
    def delete_book(self, book):
        self.books.remove(book)
    
    def delete_authors_books(self,author):
        for i in self.books:
            if i.get_author() == author:
                self.books.remove(i)
    def get_all_booksPrice(self):
        price = 0
        for i in self.books:
            price += i.get_price()
        return price
        
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)

library1.print_name()
library1.search_author_books("Paulo Coelho")
library1.search_manufactor_books("Bloomsbury")
library1.year_book("1990")
# library.delete_book(book5)
# library.print_name()
# library.delete_authors_books("Me")
# library.print_name()
library1.get_all_booksPrice()


library2 = Library()
library2.add_book(book1)
library2.add_book(book2)
library2.add_book(book3)


def compare_libraies():
    x = library1.get_all_booksPrice()
    y = library2.get_all_booksPrice()
    
    if y > x:
        print("Library2 is bigger")
    elif y < x:
        print("Library1 is bigger")
    else:
        print("Libraries are equal")
compare_libraies()
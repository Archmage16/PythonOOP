class Book():
    def __init__(self):
        self.title = 'title'
        self.year = 0
        self.author = "author"
        self.manufactor = 'manufactor'
        self.book_type = 'book_type'
        self.price = 0

    @property 
    def get_title(self):
        return self.title
    @property 
    def get_year(self):
        return self.year
    @property 
    def get_author(self):
        return self.author
    @property 
    def get_manufactor(self):
        return self.manufactor
    @property 
    def get_book_type(self):
        return self.book_type
    @property 
    def get_price(self):
        return self.price


    @get_title.setter
    def get_title(self, new_title):
        self.title = new_title
    @get_year.setter
    def get_year(self, new_year):
        if type(new_year) != int:
            return "Error year"
        else:
            self.year = new_year
            return True
    @get_author.setter
    def get_author(self, new_author):
        self.author = new_author
    @get_manufactor.setter
    def get_manufactor(self, new_manufactor):
        self.manufactor = new_manufactor
    @get_book_type.setter
    def get_book_type(self, new_book_type):
        self.book_type = new_book_type
    @get_price.setter
    def get_price(self, new_price):
        if type(new_price) != int:
            return "Error price"
        else:
            self.price = new_price
            return True

    
    
    
    def Inputs(self):
        t = input("Write a book title: ")
        self.get_title = t
        
        
        while True:
            try:
                t = int(input("Write a book year: "))
                self.get_year = t
                if t:
                    break
            except ValueError as va:
                print(f"Error: {va}")
            print("Try again. It isn't right year")

        t = input("Write a book author: ")
        self.get_author = t

        t = input("Write a book manufactor: ")
        self.get_manufactor = t

        t = input("Write a book type: ")
        self.get_book_type = t

        while True:
            try:
                t = int(input("Write a book price: "))
                self.get_price = t
                if t:
                    break
            except ValueError as va:
                print(f"Error: {va}")
            print("Try again. It isn't right price")

    
    def Print(self):
        print(f"Book title: {self.get_title}")
        print(f"Book year: {self.get_year}")
        print(f"Book author: {self.get_author}")
        print(f"Book manufactor: {self.get_manufactor}")
        print(f"Book type: {self.get_book_type}")
        print(f"Book price in tenge: {self.get_price}")

    def __format__(self, format_spec):
        res = f'|| {self.get_title} | {self.get_price} | {self.get_book_type} ||'
        print("-"*len(res))
        print("-"*len(res))
        return res

    def __str__(self):
        print(f"Book's type{self.get_title}")
        print(f"Book's{self.get_price}")
        print(f"{self.get_description}")

b1 = Book()
b1.Inputs()

print(f"{b1}")
class Car() :
    def __init__(self, volume, color,name, birthday, manuf, price):
        self.volume = volume
        self.color = color
        self.name = name
        self.birthday = birthday
        self.manuf = manuf
        self.price = price
        
    def set_name( self, name: str ):
        self.name = name
    def set_birthday( self, birthday: str ):
        self.birthday = birthday
    def set_manufactor( self, manuf: str ):
        self.manuf = manuf
    def set_price( self, price: int ): 
        self.price = price
    def set_volume( self, volume: int ):
        self.volume = volume
    def set_color( self, color: str ):
        self.color = color
        
        
        
    def get_name( self ) -> str:
        return self.name
    def get_birthday( self ) -> str:
        return self.birthday
    def get_manufactor(self) -> str:
        return self.manuf
    def get_price( self ) -> int:
        return self.price
    def get_volume(self) -> int:
        return self.volume
    def get_color(self) -> str:
        return self.color
        
    def Print(self):
        print(f"Name: {self.get_name()} ")
        print(f"Date of creating: {self.get_birthday()} ")
        print(f"Manufactor: {self.get_manufactor()} ")
        print(f"Price: {self.get_price()} tenge")
        print(f"Engine volume: {self.get_volume()} tenge")
        print(f"Cars color: {self.get_color()} tenge")
   
class Book() :
    def __init__(self, type_book, author, name, birthday, manuf, price):
        self.type_book = type_book
        self.author = author
        self.name = name
        self.birthday = birthday
        self.manuf = manuf
        self.price = price
        
    def set_name( self, name: str ):
        self.name = name
    def set_birthday( self, birthday: str ):
        self.birthday = birthday
    def set_manufactor( self, manuf: str ):
        self.manuf = manuf
    def set_price( self, price: int ):
        self.price = price
    def set_book( self, type_book: str ):
        self.type_book = type_book
    def set_author( self, author: str ):
        self.author = author
    
        
    def get_name( self ) -> str:
        return self.name
    def get_birthday( self ) -> str:
        return self.birthday
    def get_manufactor(self) -> str:
        return self.manuf
    def get_price( self ) -> int:
        return self.price
    def get_book(self) -> int:
        return self.type_book
    def get_author(self) -> str:
        return self.author
    def Print(self):
        print(f"Book name: {self.get_name()} ")
        print(f"Author: {self.get_author()} tenge")
        print(f"Date of creating: {self.get_birthday()} ")
        print(f"Manufactor: {self.get_manufactor()} ")
        print(f"Price: {self.get_price()} tenge")
        print(f"Book type: {self.get_book()} tenge")  

class Stadion() :
    def __init__(self, name, birthday, place, capacity):
        self.name = name
        self.birthday = birthday
        self.place = place
        self.capacity = capacity
        
    def set_name( self, name: str ):
        self.name = name
    def set_birthday( self, birthday: str ):
        self.birthday = birthday
    def set_place( self, place: str ):
        self.place = place
    def set_capacity( self, capacity: int ):
        self.capacity = capacity
        
    
    def get_name( self ) -> str:
        return self.name
    def get_birthday( self ) -> str:
        return self.birthday
    def get_place(self) -> str:
        return self.place
    def get_capacity( self ) -> int:
        return self.capacity
    def Print(self):
        print(f"Name: {self.get_name()} ")
        print(f"Was opened: {self.get_birthday()} ")
        print(f"Capacity: {self.get_capacity()} ")
        print(f"In: {self.get_place()}")
        
        
# a = Car("Toyota", "2009", "Japan", 5_000_000, 3.5, "black").Print()
# b = Book("Science-fiction", " J. K. Rowling", "Harry Potter", "1997", "UK", 4000).Print()
# c = Stadion("Astana, Kazahstan", 6000 ,"Barys arena", "2005").Print()
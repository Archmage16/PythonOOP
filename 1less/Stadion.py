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


stadion1 = Stadion("Olimp", "12.12.2000", "Ukraine, Kyiv", 6000)

stadion1.Print()
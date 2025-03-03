import flats

class House():
    def __init__(self):
        self.__flats = []
        self.__number_of_flats = 0
        
    @property
    def flats(self):
        return self.__flats
    @flats.setter
    def flats(self, new_flats):
        self.__flats = new_flats
    
    @property
    def number_of_flats(self):
        return self.__number_of_flats
    @number_of_flats.setter
    def number_of_flats(self, new_number_of_flats):
        self.__number_of_flats = new_number_of_flats
        
    def Input(self):
        self.number_of_flats = int(input("Quantity of flats: "))
        for i in range(self.number_of_flats):
            t = flats.Flat().Input()
            self.__flats.append(t)
            
    def __str__(self):
        res = f"\nNumber of flats: {self.number_of_flats} \n"
        for i in self.flats:
            res += f'{i}\n'
        return res
    
h1 = House()
h1.Input()
print(h1)




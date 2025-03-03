import Person1

class Flat():
    def __init__(self):
        self.__people = []
        self.__number = 0
    
    @property
    def people_list(self): return self.__people
    @people_list.setter
    def people_list(self, new_people):
        self.__people = new_people
    
    @property
    def number(self): return self.__number
    @number.setter
    def number(self, new_number):
        assert (new_number > 0) and (new_number < 1000), "Error"
        self.__number = new_number
        
    def Input(self):
        self.number = int(input("Flats number: "))
        c = int(input("Number of people: "))
        for i in range(c):
            t = Person1.Person().Input()
            self.__people.append(t)
        return self

    def __str__(self):
        res = ''
        res += f"\Flat : {self.number} \n"
        for i in self.people_list:
            # res += str(i) + "\n"
            res += f'{i}\n'
        return res


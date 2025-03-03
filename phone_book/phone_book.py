from person import Person

class PhoneBook():
    def __init__(self, person='', phone_book=[]):
        self.__person = person
        self.__phone_book = phone_book
    
    @property
    def phone_book(self):
        return self.__phone_book
    @phone_book.setter
    def phone_book(self, phone_book):
        self.__phone_book = phone_book
        
    @property
    def person(self):
        return self.__person
    @person.setter
    def person(self, person):
        self.__person = person
    
    def Inputs(self):
        number_of_contacs = int(input("Quantity of contacts: "))
        for i in range(number_of_contacs):
            t = Person()
            t.Inputs()
            self.phone_book.append(t)
    
    def __str__(self):
        result = ''
        for person in self.phone_book:
            result += str(person) + '\n'
        return result
    
    def add(self, person : Person):
        if isinstance(person, Person):
            self.phone_book.append(person)
        else:
            print('Error input')
    
    def remove(self, name):
        for person in self.phone_book:
            if person.name == name:
                self.phone_book.remove(person)
                print(self.__str__())
        return None
    
    def search_FIO(self):
        t = str(input('Write FIO: '))
        while True:
            for person in self.phone_book:
                if person.name == t:
                    print(person)
            return None
        
    def search_mobile_phone(self):
        t = str(input('Write mobile phone: '))
        while True:
            for person in self.phone_book:
                if person.mobile_phone == t:
                    print(person)
            return None
        
    def Menu(self):
        print('1. Add contact\n2. Remove contact\n3. Search by FIO \
            \n4. Search by mobile phone\n5. Show all contacts\n0. Exit\n')
        t = int(input("Choose method: "))
        while True:
            match t:
                case 1:
                    self.Inputs()
                case 2:
                    t = str(input('Write FIO: '))
                    self.remove(t)
                case 3:
                    self.search_FIO()
                case 4:
                    self.search_mobile_phone()
                case 5:
                    return self
                case 0:
                    print('Goodbye!')
                    break
    
    
pb = PhoneBook()


pb.add(Person('Marya Aleksandrovna', '123', '234', '+77015551767', 'qwerty'))
pb.add(Person('Ivan Ivanovich', '123', '234', '+77015551767', 'qwerty'))
pb.add(Person('Petr Petrovich', '123', '234', '+77015551767', 'qwerty'))
pb.add(Person('Sidor Sidorovich', '123', '234', '+77015551767', 'qwerty'))
pb.add(Person('Sidor Sidorovich', '123', '234', '+77778121369', 'qwerty'))

pb.Menu()
print(pb)


# pb.search_FIO()
# pb.search_mobile_phone()

# print(pb)
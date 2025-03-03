class Student:
    def __init__(self, name = '', major = '', diplom = ''):
        self.name = name
        self.major = major
        self.diplom = diplom

    def show(self):
        print(f"Name = {self.name}")
        print(f"Major = {self.major}")
        print(f"Diplom = {self.diplom}")
        print('-' * 20)
    

class Aspirant(Student):
    def __init__(self, name = '', major_st = '', diplom_st = '', major_asp = '', diplom_asp = '', student : Student = None):
        
        if student is not None:
            super().__init__(student.name, student.major, student.diplom)
            self.diplom_asp = diplom_asp
            self.major_asp = major_asp
        else:
            super().__init__(name, major_st, diplom_st)
            self.diplom_asp = diplom_asp
            self.major_asp = major_asp

    

    def show(self):
        super().show()
        print(f'Name = {self.name}')
        print(f'Aspirant major  = {self.major_asp}')
        print(f'Diplom aspirant = {self.diplom_asp}')
        

st1 = Student("Sasha", 'Programmer', 'Flusk')
# st1.show()

# asp1 = Aspirant("Sasha", 'Programmer', 'Flusk', 'Engineer', 'Computer engineering')
# asp1.show()

asp2 = Aspirant(student=st1, diplom_asp='Computer engineering', major_asp='Engineer')
asp2.show()
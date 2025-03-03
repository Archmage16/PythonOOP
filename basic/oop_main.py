# Принципы ООП
# 1) Инкапсуляция
# 2) Полиморфизм
# 3) Наследование
# 4) Абстракция

class Students():
    # Static variable
    Group_name = 'Py_242'
    
    def __init__(self, name, age):
        # Changeable variables
        self.name = name
        self.__age = age   


    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        self.__age = new_age

    def print(self):
        b = f'| Student name = {self.name} | Student age = {self.get_age()} |'
        print(len(b)*"-")
        print(b)
        print(len(b)*"-")
        

a = Students("mus", 16)
# a.print()
# a.set_age(20)
# a.print()

### Weird situation
a.__age = '2'
print(a.__age)
print(a.get_age())
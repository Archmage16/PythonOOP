class Person():
    def __init__(self):
        self.__name = ""
        self.__age = 1

    # @property
    # def all_info(self) -> tuple:
    #     return tuple([self.name_func, self.age_func])
    # @all_info.setter
    # def all_info(self, param : tuple):
    #     self.name_func = param[0]
    #     self.age_func = param[1]
    
    @property
    def name_func(self):
        return self.__name 
    @property
    def age_func(self):
        return self.__age 
    @name_func.setter
    def name_func(self, new_name):
        self.__name = new_name
    @age_func.setter
    def age_func(self, new_age):
        if new_age < 0 or new_age > 120:
            print("Wrong age")
        else:
            self.__age = new_age

    def Input(self):
        t = input("Write name: ")
        self.name_func = t
        t = int(input("Write age: "))
        self.age_func = t
        return self
    def Print_all_info(self):
        print(f"Person name: {self.name_func}")
        print(f"Person age: {self.age_func}")
        print()
        
        
    # def __str__(self):
    #     res = ''
    #     res += 'Name' + str(self.name_func) + '\n'
    #     res += 'Age' + str(self.age_func)
    #     return res

    def __format__(self, format_spec):
        res = f'| {self.name_func} || {self.age_func} |'
        return res
    
    

    
# p1 = Person('Petr', 20)
# p2 = Person('Marya', 19)
# p3 = Person('Vasiliy', 35)
# p4 = Person('Dary', 40)


# p1.Print_all_info()
# p2.Print_all_info()
# p3.Print_all_info()
# p4.Print_all_info()
# print(f"{p1}")
# print(f"{p2}")
# print(f"{p3}")
# print(f"{p4}")
class Сertificate:
    def __init__(self, name = '', age = 0, ID = ''):
        self.__name = name
        self.__age = age
        self.__ID = ID
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
        
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID):
        self.__ID = ID
    
    def Print(self):
        print(f"{self.name} is {self.age} years old. ID: {self.ID}")
        

class ForeignPassport(Сertificate):
    def __init__(self, name='', age=0, ID='', number_of_Pasport='', VISA_ctn=0):
        super().__init__(name, age, ID)
        self.__number_of_Pasport = number_of_Pasport
        self.__VISA_ctn = VISA_ctn
    
    @property
    def number_of_Pasport(self):
        return self.__number_of_Pasport
    @number_of_Pasport.setter
    def number_of_Pasport(self, number_of_Pasport):
        self.__number_of_Pasport = number_of_Pasport
    
    @property
    def VISA_ctn(self):
        return self.__VISA_ctn
    @VISA_ctn.setter    
    def VISA_ctn(self, VISA_ctn):
        self.__VISA_ctn = VISA_ctn
    
    
    def Print(self):
        # print(f"{self.name} is {self.age} years old. ID: {self.ID}.")
        super().Print()
        print(f"Passport number: {self.number_of_Pasport}.")
        print(f"Number of VISA: {self.VISA_ctn}")
        

f1 = ForeignPassport("John", 25, "111222333444", "AB123456", 5)
f1.Print()
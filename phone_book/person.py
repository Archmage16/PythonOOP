class Person():
    def __init__(self, name='', home_phone='None',office_phone='234', mobile_phone='+7-701-XXX-XXXX', add_info=''):
        self.__name = name
        self.__home_phone = home_phone
        self.__office_phone = office_phone
        self.__mobile_phone = mobile_phone
        self.__add_info = add_info
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def home_phone(self):
        return self.__home_phone
    @home_phone.setter
    def home_phone(self, home_phone):
        self.__home_phone = home_phone
        
    @property
    def office_phone(self):
        return self.__office_phone
    @office_phone.setter
    def office_phone(self, office_phone):
        self.__office_phone = office_phone
        
    @property
    def mobile_phone(self):
        return self.__mobile_phone
    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        self.__mobile_phone = mobile_phone
        
    @property
    def add_info(self):
        return self.__add_info
    @add_info.setter
    def add_info(self, add_info):
        self.__add_info = add_info
    
    def Inputs(self):
        self.name = input('Write FIO: ')
        self.home_phone = input('Write home phone: ')
        self.office_phone = input('Write office phone: ')
        self.mobile_phone = input('Write mobile phone: ')
        self.add_info = input('Write additional information: ')
    
    def __str__(self):
        return f'| Name: {self.name:15} | Mobile phone: {self.mobile_phone:15}|'
    
    
# p1 = Person()
# p1.Inputs()
# print(p1)
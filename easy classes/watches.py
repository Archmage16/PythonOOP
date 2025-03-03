class Watch():
    def __init__(self):
        self.__name = "name"
        self.__manuf = "manuf"
        self.__year = 1900
        self.__price = 5000
        self.__wtype = "Другие"
    
    @property
    def get_name(self):
        return self.__name
    @property
    def get_manuf(self):
        return self.__manuf
    @property
    def get_year(self):
        return self.__year
    @property
    def get_price(self):
        return self.__price
    @property
    def get_type(self):
        return self.__wtype
    
    @get_name.setter
    def get_name(self, new_name):
        self.__name = new_name
    @get_manuf.setter
    def get_manuf(self, new_manuf):
        self.__manuf = new_manuf
    @get_year.setter
    def get_year(self, new_year):
        self.__year = new_year
    @get_price.setter
    def get_price(self, new_price):
        self.__price = new_price
    @get_type.setter
    def get_type(self, new_type):
        watches_types = ["Наручные", "Настенные","Другие"]
        for i in watches_types:
            if new_type == i:
                self.__wtype = i
                return True
            else:
                return False
       
    
    def inputs(self):
        t = input("Напиши название часов: ")
        self.get_name = t
        t = input("Напиши производителя часов: ")
        self.get_manuf = t
        t = int(input("Напиши год выпуска часов: "))
        self.get_year = t
        t = int(input("Напиши цену часов: "))
        self.get_price = t
        while True:
            try:
                t = input("Напиши тип часов: ")
                self.get_type = t
                if t:
                    break
            except ValueError as va:
                print("Error")
            print("Try again. It isn't right")
    
    def __format__(self, format_spec):
        res = f'|| {self.get_name} | {self.get_manuf} | {self.get_price} | {self.get_type}||'
        p =  "Часы который есть y нас"
        print("-"*len(res))
        print(p)
        print("-"*len(res))
        return res
    
    
    def Print_all(self):
        print(f"Название часов - {self.get_name}")
        print(f"Производитель часов {self.get_manuf}")
        print(f"Год выпуска часов: {self.get_year}")
        print(f"Цена часов {self.get_price}")
        print(f"Тип часов {self.get_type}")
        
w1 = Watch()
w1.inputs()
w1.Print_all()
# print(f"{w1}")
class City():
    def __init__(self):
        self.name = ''
        self.country = ''
        self.population = 0
        self.post = ''
        self.phone = ''
        
    
    def set_name(self, name):
        self.name = name
    def set_country(self, country):
        self.country = country
    def set_populaiton(self,population):
        if population > 100000:
            self.population = population
            return True
        else:
            print("It isn't city")
            return False    
    def set_post(self,post):
        if len(self.post) == 6:
            self.post = post
            return True
        else:
            print("Error post code")
            return False    
    def set_phone(self,phone : str):
        if len(self.post) == 3 and phone.isdigit():
            self.phone = phone
            return True
            
        else:
            print("Error phone code")
            return False    
            
    def get_name(self):
        return self.name          
    def get_country(self):
        return self.country
    def get_population(self):
        return self.population
    def get_post(self):
        return self.post
    def get_phone(self):
        return self.phone
    
    
    def inputs(self):
        # self.name = input("Write a city name")
        # self.country = input("Write a city country")
        # self.population = int(input("Write a city population"))
        # self.post = input("Write a city post index")
        # self.phone = input("Write a city phone code")
        
        t = input("Write a city name: ")
        self.set_name(t)
        t = input("Write a city country: ")
        self.set_country(t)
        
        while True:
            try:
                t = int(input("Write a city population: "))
                if self.set_populaiton(t):
                    break
            except ValueError as va:
                print("Error")
            print("Try again. It isn't city")
        
        while True:
            try:
                t = input("Write a city post index: ")
                if self.set_post(t):
                    break
            except ValueError as va:
                print("Error")
            print("Try again. It isn't right post code")      
                
        while True:
            try:
                t = input("Write a city phone code: ")
                if self.set_phone(t):
                    break
            except ValueError as va:
                print("Error")
            print("Try again!")          
        
    def Print(self):
        print(f"City name{self.get_name()}")
        print(f"Country{self.get_country()}")
        print(f"Population: {self.get_population()}")
        print(f"Почтовый индекс{self.get_post()}")
        print(f"Телефонный код {self.get_phone()}")

rand_city = City()
rand_city.inputs()


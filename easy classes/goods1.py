class Good():
    def __init__(self):
        self.name = 'name'
        self.price = 0
        self.manufactor = 'manufactor'
        self.quantity = 0
        self.description = 'description'

    @property 
    def get_name(self):
        return self.name
    @property 
    def get_quantity(self):
        return self.quantity
    @property 
    def get_manufactor(self):
        return self.manufactor
    @property 
    def get_description(self):
        return self.description
    @property 
    def get_price(self):
        return self.price


    @get_name.setter
    def get_name(self, new_name):
        self.name = new_name
    @get_quantity.setter
    def get_quantity(self, new_quantity):
        if type(new_quantity) != int:
            return "Error quantity"
        else:
            self.quantity = new_quantity
            return True
    @get_manufactor.setter
    def get_manufactor(self, new_manufactor):
        self.manufactor = new_manufactor
    @get_description.setter
    def get_description(self, new_description):
        self.description = new_description
    @get_price.setter
    def get_price(self, new_price):
        self.price = new_price

    
    
    
    def Inputs(self):
        t = input("Write a good name: ")
        self.get_name = t
        t = input("Write a description: ")
        self.get_description = t
        
        t = input("Write a manufactor: ")
        self.get_manufactor = t
        while True:
            try:
                t = int(input("Write a right quantity: "))
                self.get_quantity = t
                if t:
                    break
            except ValueError as va:
                print(f"Error: {va}")
            print("Try again. It isn't right quantity")

        

        while True:
            try:
                t = int(input("Write a price: "))
                self.get_price = t
                if t:
                    break
            except ValueError as va:
                print(f"Error: {va}")
            print("Try again. It isn't right price")

    
    def Print(self):
        print(f"Good name: {self.get_name}")
        print(f"Good quantity: {self.get_quantity}")
        print(f"Good manufactor: {self.get_manufactor}")
        print(f"Good type: {self.get_description}")
        print(f"Good price in tenge: {self.get_price}")

    def __format__(self, format_spec):
        res = f'|| {self.get_name} | {self.get_price} | {self.get_description} ||'
        print("-"*len(res))
        print("-"*len(res))
        return res
    def __str__(self):
        print(f"Good's type: {self.get_title}")
        print(f"Good's price: {self.get_price}")
        print(f"Good's description: {self.get_description}")

g1 = Good()
g1.Inputs()
g1.Print()
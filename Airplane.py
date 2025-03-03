class Airplane():
    def __init__(self, type_a = "none", quantity = 0, max_quantity = 1000):
        self.__type = type_a
        self.__quantity = quantity
        self.__max_quantity = max_quantity
        
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        self.__type = value
    
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    
    @property
    def max_quantity(self):
        return self.__max_quantity
    @max_quantity.setter
    def max_quantity(self, value):
        self.__max_quantity = value
    
    
    def __eq__(self,value):
        return self.type == value.type
    
    
    
    def __add__(self,value):
        a = Airplane()
        a.quantity = self.quantity + value.quantity
        return a
    def __sub__(self,value):
        a = Airplane()
        a.quantity = self.quantity - value.quantity
        return a
    def __iadd__(self,value):
        self.quantity += value.quantity
        return self
    def __isub__(self,value):
        self.quantity -= value.quantity
        return self
    
    
    
    def __gt__(self,value):
        return self.max_quantity > value.max_quantity
    def __lt__(self,value):
        return self.max_quantity < value.max_quantity
    def __ge__(self,value):
        return self.max_quantity >= value.max_quantity
    def __le__(self,value):
        return self.max_quantity <= value.max_quantity
    
    def __str__(self):
        return f"{self.type} {self.quantity} {self.max_quantity}"

a1 = Airplane("Boeing", 100, 500)
a2 = Airplane("Boeing-474", 200, 500)
print(f"{a1}")
print(f"{a2}")
# print(a1.type == a2.type)

# print(a1.max_quantity + a2.max_quantity)
# print(a1.max_quantity - a2.max_quantity)
# a1.quantity += a2.quantity
# print(a1.quantity)
# a1.quantity -= a2.quantity
# print(a1.quantity)

# print(a1.max_quantity > a2.max_quantity)
# print(a1.max_quantity < a2.max_quantity)
# print(a1.max_quantity >= a2.max_quantity)
# print(a1.max_quantity <= a2.max_quantity)




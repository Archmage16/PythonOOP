class Flat():
    def __init__(self, area = 0, price = 0):
        self.__area = area
        self.__price = price
        
    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self, value):
        self.__area = value
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value
        
    def __eq__(self, value):
        return self.__area == value.__area
    def __ne__(self, value):
        return self.__area != value.__area
    
    def __gt__(self, value):
        return self.__price > value.__price
    def __lt__(self, value):
        return self.__price < value.__price
    def __ge__(self, value):
        return self.__price >= value.__price
    def __le__(self, value):
        return self.__price <= value.__price
    
    def __str__(self):
        return f"Area: {self.__area} Price: {self.__price}"
    
f1 = Flat(56, 21000000)
f2 = Flat(43, 14000000)

print(f1)
print(f2)

print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
print(f1 >= f2)
print(f1 <= f2)

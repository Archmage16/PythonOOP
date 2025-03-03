class Circle():
    def __init__(self, radius):
        self.__radius = radius
        self.__length = 2 * 3.14 * radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Error input")
        else:
            self.__radius = value
       
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, value):
        self.__length = value            
    


    def __eq__(self, value):
        return self.__radius == value.__radius
    
    def __gt__(self, value):
        return self.__length > value.__length
    def __lt__(self, value):
        return self.__length < value.__length
    def __ge__(self, value):
        return self.__length >= value.__length
    def __le__(self, value):
        return self.__length <= value.__length
    
    
    def __add__(self, value):
        return Circle(self.__radius + value.__radius)
    
    def __sub__(self, value):
        return Circle(self.__radius - value.__radius)

    def __iadd__(self, value):
        self.__radius += value.__radius
        return self
    def __isub__(self, value):
        self.__radius -= value.__radius
        return self


c1 = Circle(9)
c2 = Circle(4)

# print(c1 == c2)
# print(c1 > c2)
# print(c1 < c2)
# print(c1 >= c2)
# print(c1 <= c2)
# print(c1 + c2)
# print(c1 - c2)

# c1 = c1 + c2
# print(c1.radius)
# c1 = c1 - c2
# print(c1.radius)
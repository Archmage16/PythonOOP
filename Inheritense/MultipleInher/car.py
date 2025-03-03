class Part:
    def __init__(self, ):
        self.name = ""
        self.manuf = ""
        self.price = 0
    
    def Print(self):
        print(f"Part name : {self.name}")
        print(f"Part manuf : {self.manuf}")
        print(f"Part price : {self.price}")

class Wheel(Part):
    def __init__(self):
        Part.__init__(self)
        self.diametr = 28
    
    def Print(self):
        # Part.Print(self)
        print(f"Wheels diametr = {self.diametr}")

class Engine(Part):
    def __init__(self):
        Part.__init__(self)
        self.power = 323
    def Print(self):
        # Part.Print(self)
        print(f"Engine's power = {self.power}")

class Kuzov(Part):
    def __init__(self):
        Part.__init__(self)
        self.color = "black"
    def Print(self):
        # Part.Print(self)
        print(f"Car's color = {self.color}")



class Car(Wheel, Engine, Kuzov):
    def __init__(self):
        Wheel.__init__(self)
        Engine.__init__(self)
        Kuzov.__init__(self)
        self.name = "Camry"
        self.manuf = "Japan"
        self.price = 6500000
    def Print(self):
        Part.Print(self)
        Wheel.Print(self)
        Engine.Print(self)
        Kuzov.Print(self)

car1 = Car()
car1.Print()

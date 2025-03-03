class Shape:
    # def __init__(self):
    pass

class Square(Shape):
    def __init__(self,a):
        self.a = a
    def Print(self):
        print(f"Square's side = {self.a}")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def Print(self):
        print(f"Circle's radius = {self.r}")

class Circle_in_Sq(Circle, Square):
    def __init__(self, a, r):
        Square.__init__(self, a)
        Circle.__init__(self, r)
    
    def Print(self):
        Square.Print(self)
        Circle.Print(self)
        if self.a == (self.r * 2):
            print("Круг вписан в квадрат!")
        else:
            print("Круг не может быть вписан в квадрат!")


cis1 = Circle_in_Sq(12,6)
cis1.Print()
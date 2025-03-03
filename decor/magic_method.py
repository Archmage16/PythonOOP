class Frac():
    def __init__(self, a=0, b=1, name='no'):
        self.__a = a
        self.__b = b
        self.__name = name
    
    @property
    def get_a(self): return self.__a
    @get_a.setter
    def get_a(self, val): self.__a = val
    
    @property
    def get_b(self): return self.__b
    @get_b.setter
    def get_b(self, val): 
        if val != 0: self.__b = val
        else: print("Error, ZeroDivisionError")
        
    @property
    def get_name(self): return self.__name
    @get_name.setter
    def get_name(self, val): self.__name = val
    
    def __str__(self):
        res = f"{self.get_name} = {self.get_a} / {self.get_b}"
        return res
    def __add__(self,other):
        res = Frac()
        res.get_b = self.get_b * other.get_b
        res.get_a = self.get_a * other.get_b + self.get_b * other.get_a
        res.get_name = self.get_name + "+" + other.get_name
        return res
    
    def __sub__(self,other):
        res = Frac()
        res.get_b = self.get_b * other.get_b
        res.get_a = self.get_a * other.get_b - self.get_b * other.get_a
        res.get_name = self.get_name + "-" + other.get_name
        return res
    
    def __mul__(self,other):
        res = Frac()
        res.get_a = self.get_a * other.get_a 
        res.get_b = self.get_b * other.get_b
        res.get_name = self.get_name + "*" + other.get_name
        return res
    
    def __truediv__(self,other):
        res = Frac()
        res.get_a = self.get_a * other.get_b 
        res.get_b = self.get_b * other.get_a
        res.get_name = self.get_name + "*" + other.get_name
        return res

f1 = Frac(1,2,'X')
print(f1)
f2 = Frac(1,4,'Y')
print(f2)
f = f1 / f2 # f = f1 * f2 # f = f1 - f2 # f = f1 + f2
print(f)

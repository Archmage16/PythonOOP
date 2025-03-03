class Pets():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Info(self):
        print(f"I am {self.name}. I am {self.age} years")

    def show(self):
        print("I don't know what language I speak")
        
class Cat(Pets):  
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
          
    def show(self):
        print("Meow Meow")


  
        
Owner1 = Pets("Tom", 20)
Owner1.Info()


Cat1 = Cat("Bill", 34, 'Black')
Cat1.show()

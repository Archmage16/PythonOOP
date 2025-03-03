class Employer:
    def __init__(self, name):
        self.name = name
        self.job = "Employer"
        
    def Print(self):
        print(f"{self.name} is {self.job}")



class President(Employer):
    def __init__(self, name):
        super().__init__(name)
        self.job = "President"
        
    def Print(self):
        print(f"{self.name} is {self.job}")

class Manager(Employer):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Manager"
        
    def Print(self):
        print(f"{self.name} is {self.job}")

class Worker(Employer):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Worker"
        
    def Print(self):
        print(f"{self.name} is {self.job}")
        
    


p1 = President("John")
p1.Print()

m1 = Manager("Tom", )
m1.Print()

w1 = Worker("Alice")
w1.Print()

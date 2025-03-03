class Pet:
    def __init__(self,name, age):
        print("PET")
        self.name = name
        self.age = age
    def Print(self):
        print(f"Cat's Name: {self.name}")
        print(f"Cat's age: {self.age}")


class Cat(Pet):
    def __init__(self, name, age, em):
        print("Cat")
        self.em = em
        Pet.__init__(self, name, age)
    def Print(self):
        super().Print()
        print(f"Cat ate {self.em} mouse")


class Dog(Pet):
    def __init__(self, name, age, cnt):
        print("Dog")
        self.cnt = cnt
        Pet.__init__(self, name, age)
    def Print(self):
        super().Print()
        print(f"Dog know {self.cnt} command")





class CatDog(Cat, Dog):
    def __init__(self, name, age):
        Cat.__init__(self, name, age, 10)
        Dog.__init__(self, name, age, 7)
    def Print(self):
        Cat.Print(self)
        Dog.Print(self)


cd = CatDog('Котопёс', 5)
cd.Print()
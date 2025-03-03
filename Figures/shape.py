import json, math

class Shape:
    def __init__(self, name = ''):
        self.name = name
        self.x1_coord = 0
        self.y1_coord = 0
        
        
    def Area(self):
        pass
    def Show(self):
        print(f"{self.name}. Area: {self.Area()}")
        print(f"Coordinates: ({self.x1_coord}, {self.y1_coord}), ({self.x2_coord}, {self.y1_coord}))")
        
    def Save_to_JSON(self):
        try:
            with open('this.json', "r") as f_json:
                data = json.load(f_json)  
                if not isinstance(data, list):  
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
                data = []    
        new_data = {
            "name": self.name,
            "x1_coord": self.x1_coord,
            "y1_coord": self.y1_coord,
            "Area": self.Area()
        }
        data.append(new_data)
        with open(f"this.json", "w") as f_json:            
            json.dump(data, f_json, indent=4)
        print("Saved")
            
    def Load_from_JSON(self):
        data = ''
        with open(f"this.json", "r") as f_json:
            data = json.load(f_json)
            print(data)
    


class Square(Shape):
    def __init__(self, x1, y1, a):
        super().__init__(name = "Square")
        self.x1_coord = x1
        self.y1_coord = y1
        self.a = a
        
    def Area(self):
        self.area = self.a ** 2
        return self.area
    def Show(self):
        super().Show()
    def Save_to_JSON(self):
        super().Save_to_JSON()
    def Load_from_JSON(self):
        super().Load_from_JSON()


sq1 = Square(1, 3, 3)
# sq1.Save_to_JSON()
# sq1.Load_from_JSON()



class Rectangle(Shape):
    def __init__(self, x1, y1, a, b):
        super().__init__(name = "Rectangle")
        self.x1_coord = x1
        self.y1_coord = y1
        self.a = a
        self.b = b

    def Area(self):
        return self.a * self.b
    def Show(self):
        super().Show()

    def Save_to_JSON(self):
        super().Save_to_JSON()
        
    def Load_from_JSON(self):
        super().Load_from_JSON()

rec1 = Rectangle(1, 4, 6, 4)
# rec1.Save_to_JSON()
# rec1.Load_from_JSON()
        

class Circle(Shape):
    def __init__(self, x_center, y_center, r):
        super().__init__(name = "Circle")
        self.x1_coord = x_center
        self.y1_coord = y_center
        self.radius = r
        
    def Area(self):
        S = (math.pi * (self.radius**2))
        return S
    def Show(self):
        super().Show()

    def Save_to_JSON(self):
        super().Save_to_JSON()
        
    def Load_from_JSON(self):
        super().Load_from_JSON()


c1 = Circle(4, 2, 5)
# c1.Save_to_JSON()
# c1.Load_from_JSON()


class Ellipse(Shape):
    def __init__(self, x1, y1, r, R):
        super().__init__(name = "Ellipse")
        self.x1_coord = x1
        self.y1_coord = y1
        self.R = R
        self.r = r
        
    def Area(self):
        S = math.pi * self.R * self.r
        return S
    def Show(self):
        super().Show()

    def Save_to_JSON(self):
        super().Save_to_JSON()
        
    def Load_from_JSON(self):
        super().Load_from_JSON()

ec1 = Ellipse(0, 0, 4, 7)
# ec1.Save_to_JSON()
# ec1.Load_from_JSON()

try:
    with open('this.json', 'r') as f:
        data = json.load(f)
        for i in data:
            print(i)
except:
    print("None")
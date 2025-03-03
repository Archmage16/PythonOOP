import math

class Figures_area():
    
    def Herons_Formula(self, a, b ,c):
        p = (a+b+c) / 2
        ans = math.sqrt(p * (p-a) * (p-b) * (p-c))
        return ans
    def With_sinus(self, a,b,G):
        # G = pi/number - radians
        ans = 1/2 * a * b * math.sin(G)
        return ans
    def With_height(self, a,h):
        ans = a*h*1/2
        return ans
    
    def Triangle(self,a,b,c,G,h):
        
        if a == 0:
            return "Error"
        elif b == 0 or c == 0:
            print(self.With_height(a,h))
        elif c == 0:
            print(self.With_sinus(a,b,G))
        else:
            print(self.Herons_Formula(a, b, c))

fa=Figures_area()
a = fa.Triangle(10,11,12,(math.pi/3), 14)

import random as rd

class Element:
    next_id = 1

    def __init__(self):
        self.id = Element.next_id
        Element.next_id += 1
        self.value = rd.randint(1,20)
    

    def __str__(self):
        return f"{self.id} : {self.value}"


    def __lt__(self, other) -> bool:
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value

list1 = []    

for i in range(10):
    t  = Element()
    list1.append(t.value)

s = ', '.join(str(i) for i in list1)
print(s)

set1 = set(list1)
s = ', '.join(str(i) for i in set1)
print(s)

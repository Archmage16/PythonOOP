import random as rd

class Stack(list):
    def push(self, value):
        self.append(value)
    def pop(self):
        return super().pop()
    def top(self):
        return self[-1]

    def __len__(self):
        return super().__len__()

    def __str__(self):
        return super().__str__()

s1 = Stack()
for i in range(10):
    s1.push(rd.randint(1,100))
print(f"{s1}")
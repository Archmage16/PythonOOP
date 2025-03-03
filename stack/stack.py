import random as rd


class Stack:
    def __init__(self, depth = 100):
        self.__depth = depth
        self.__top = 0
        self.__data = [0] * depth

    @property
    def depth(self):
        return self.__depth
    @depth.setter
    def depth(self,new_depth):
        if new_depth == self.__depth: return
        if new_depth > self.__depth: 
            self.__data = self.__data + [0] * (new_depth - self.__depth)
        elif new_depth >= self.__top:
            self.__data = self.__data[:new_depth]
        else:
            self.__data = self.__data[:new_depth]
            self.__top = new_depth
        self.__depth = new_depth


    @property
    def count(self) -> int:
        return self.__top

    @property
    def isEmpty(self) -> bool:
        return self.__top == 0 

    @property
    def isFull(self) -> bool:
        return self.__top == self.__depth 

    def push(self, value):
        if self.__top >= self.__depth:
            print("Stack is overflow")
            # raise Exception("Stack is overflow")

            self.depth = int((self.__depth + 1) * 1.5)

        self.__data[self.__top] = value
        self.__top += 1

    def pop(self):
        if self.__top <= 0:
            print("Error. Under overflow !!!")
        self.__top -=1
        value = self.__data[self.__top]
        return value

    def top(self):
        ind = self.__top - 1
        return self.__data[ind]







st1 = Stack(10)
for i in range(10):
    t = rd.randint(1, 20)
    print(t, end=', ')
    st1.push(t)
print()

for i in range(10):
    t = st1.pop()
    print(t, end=', ')
print()
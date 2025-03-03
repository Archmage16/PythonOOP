import random as rd

class Queue:
    def __init__(self, capacity = 100):
        self.__capacity = capacity
        self.__data = [" "] * capacity
        self.__count = 0
    
    @property
    def count(self) : return self.__count
    @property
    def capacity(self) -> int : return self.__capacity 
    
    def set_capacity(self, new_capa):
        if new_capa > self.capacity:
            size = (new_capa - self.capacity)
            self.__data = self.__data + [' '] * size
        elif new_capa > self.count:
            self.__data = self.__data[:new_capa]
        else:
            print("Error. You cut real datas")
            self.__data = self.__data[:new_capa]
            self.count = new_capa
        self.__capacity = new_capa
    @property
    def isEmpty(self) -> bool:
        return self.count == 0
    @property
    def isFull(self) -> bool:
        return self.count == self.capacity


    def enQueue(self, value):
        if self.__count >= self.__capacity:
            print("Queue is full")
            self.set_capacity(self.__capacity * 2 + 1)
        self.__data[self.__count] = value
        self.__count += 1
        return self.count


    def deQueue(self):
        if self.isEmpty:
            print("Queue is empty!!!")
        self.__count -= 1
        result = self.__data[0]

        # del self.__data[0]
        # self.__data = [' ']

        self.__data = self.__data[1:] + [' ']
        return result
    
    def Show(self):
        print(f"[{self.capacity}]/{self.count} : {self.__data}")


q1 = Queue(capacity = 10)

for i in range(12):
    t = rd.randint(ord("A"), ord("Z"))
    sym = chr(t)
    q1.enQueue(sym)
    q1.Show()
print("-" * 20)

while not q1.isEmpty:
    t = q1.deQueue()
    print(t, end=',')
print()
q1.Show()